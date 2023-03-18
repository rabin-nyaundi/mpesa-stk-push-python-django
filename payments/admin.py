from django.contrib import admin
from .models import MpesaPayment, UserProfile
from django.contrib.auth.models import User


# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "referrence_id",
        "trans_id",
        "amount",
        "result_code",
        "payment_status",
        "transaction_date",
        "response_desc",
        "result_desc",
    )


# class UserAdmin(admin.ModelAdmin):
#     list_display = "__all__"


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "phone_number")


admin.site.register(MpesaPayment, PaymentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(User, UserAdmin)
