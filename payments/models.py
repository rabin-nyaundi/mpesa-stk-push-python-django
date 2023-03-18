from django.db import models
from django.contrib.auth.models import User
from .enums import PAYMENT_STATUS
from dataclasses import dataclass
from enum import Enum


class PaymentStatus(str, Enum):
    INITIATING = "INITIATING"
    PENDING = "PENDING"
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


@dataclass
class Payment:
    status: PaymentStatus


class MpesaPayment(models.Model):
    phone_number = models.CharField(("Phone Number"), max_length=20)
    referrence_id = models.CharField(("Refrence ID"), max_length=255)
    trans_id = models.CharField(("Mpesa Transaction ID"), max_length=255, default=None, null=True)
    merchant_request_id = models.CharField(("Merchant Request ID"), max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    checkout_request_id = models.CharField(("Checkout Request ID"), max_length=120)
    response_code = models.CharField(max_length=10, null=True, blank=True)
    response_desc = models.TextField(max_length=255, null=True, blank=True)
    customer_message = models.TextField(max_length=255, null=True, blank=True)
    result_desc = models.TextField(max_length=255, null=True, blank=True)
    result_code = models.CharField(max_length=10, null=True, blank=True)
    payment_status = models.CharField(max_length=60, choices=PAYMENT_STATUS, default="INITIATING")
    transaction_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Mpesa Payments"
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.phone_number} - {self.amount}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    phone_number = models.CharField(max_length=13, null=False, blank=False)

    class Meta:
        verbose_name_plural = "User Profile"

    def __str__(self) -> str:
        return f"{self.user_id} - {self.phone_number}"
