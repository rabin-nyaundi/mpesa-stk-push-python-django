from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from mpesa.mpesa import MpesaAPI
from .models import MpesaPayment
from .enums import *
from utils.utils import convert_string_to_datetime, validate_email
from uuid import uuid4
from mpesa_stk_push.settings import MPESA_CALLBACK_URL
from .models import Payment, PaymentStatus, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    return redirect("/")


def view_register_user(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        email_address = request.POST.get("email_address")
        password = request.POST.get("password")

        user = User()
        user.email = email_address
        user.username = email_address
        user.set_password(password)
        user.save()

        user_profile = UserProfile()
        user_profile.user = user
        user_profile.phone_number = phone_number
        user_profile.save()

        return redirect("sign-in")

    return render(request, "../templates/auth/register.html")


def view_login_user(request):
    if request.user.is_authenticated:
        return redirect("initiate-payment")

    if request.method == "POST":
        email_address = request.POST.get("email_address")
        password = request.POST.get("password")

        if not validate_email(email_address):
            messages.error(request, "Invalid email address")
            return redirect("sign-in")

        if len(password) < 6:
            messages.error(request, "Password too short")
            return redirect("sign-in")

        user = authenticate(request, username=email_address, password=password)
        if user:
            login(request, user)
            request.session["user"] = user.user_profile.phone_number
            print(user.user_profile.phone_number)
            return redirect("initiate-payment")
        else:
            messages.error(request, "Invalid credeantials provided")
            return redirect("sign-in")

    return render(request, "../templates/auth/login.html")


def view_logout_user(request):
    logout(request)
    return redirect("sign-in")


@login_required
def view_update_user_phone_number(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        user = User.objects.get(pk=request.user.id)
        if user:
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.phone_number = phone_number
            user_profile.save()
            print(user_profile.phone_number)
            request.session["user"] = user_profile.phone_number
            return redirect("initiate-payment")
        else:
            messages.error(request, "Failed!")
            return HttpResponse("done")
    return render(request, "../templates/auth/edit-profile.html")


@login_required
def initiate_payment(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        amount = request.POST["amount"]

        callback_url = f"{MPESA_CALLBACK_URL}/mpesa/stk-results/"

        mpesa = MpesaAPI()
        response = mpesa.initiate_stk_push(phone_number, amount, callback_url)
        print(response)

        payment = MpesaPayment()
        payment.phone_number = phone_number
        payment.amount = amount
        payment.referrence_id = uuid4()
        payment.checkout_request_id = response.get("CheckoutRequestID")
        payment.mpesa_receipt_no = response.get("MpesaReceiptNumber")
        payment.customer_message = response.get("CustomerMessage")
        payment.response_desc = response.get("ResponseDescription")
        payment.merchant_request_id = response.get("MerchantRequestID")
        payment.response_code = response.get("ResponseCode")
        payment.save()

        messages.info(request, "STK push initiated successfully. Enter your pin in the pop up to continue.")

        return redirect("initiate-payment")
    return render(request, "payment.html")


@login_required
def stk_success(request, payment_id):
    payment = MpesaPayment.objects.get(id=payment_id)
    return render(request, "success.html", {"payment": payment})


def update_stk_results(body):
    merchant_request_id = body["MerchantRequestID"]
    checkout_request_id = body["CheckoutRequestID"]
    result_code = body["ResultCode"]
    result_desc = body["ResultDesc"]

    mpesaPayment = MpesaPayment.objects.filter(
        merchant_request_id=merchant_request_id, checkout_request_id=checkout_request_id
    ).first()

    if mpesaPayment:
        mpesaPayment.result_code = result_code
        mpesaPayment.result_desc = result_desc
        mpesaPayment.save()

    if result_code == 0 or result_code == "0":
        items = body["CallbackMetadata"]["Item"]

        amount = [element for element in items if element["Name"] == "Amount"][0]["Value"]
        trans_id = [element for element in items if element["Name"] == "MpesaReceiptNumber"][0]["Value"]
        trans_date = [element for element in items if element["Name"] == "TransactionDate"][0]["Value"]

        mpesaPayment.payment_status = "SUCCESS"
        mpesaPayment.trans_id = trans_id
        mpesaPayment.transaction_date = convert_string_to_datetime(str(trans_date))
        mpesaPayment.save()
        res = {"ResultCode": 0, "ResultDesc": "Accepted"}
        return res
    if result_code == 1032:
        mpesaPayment.payment_status = "CANCELED"
        mpesaPayment.save()
        res = {"ResultCode": 0, "ResultDesc": "Accepted"}
        return res

    else:
        print("Else", result_code)
        mpesaPayment.payment_status = "FAILED"
        mpesaPayment.save()
        res = {"ResultCode": 0, "ResultDesc": "Canceled"}
    return res


@login_required
def view_all_payments(request):
    if request.user.is_authenticated and request.user.is_superuser:
        context = {}
        payments = MpesaPayment.objects.all()
        context["payments"] = payments
        return render(request, "../templates/dashboard/index.html", context)
    else:
        messages.error(request, "Failed! You don't have the rights")
        return redirect("initiate-payment")
