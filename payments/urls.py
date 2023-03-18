from django.urls import path
from mpesa.api import stk_push_results
from .views import (
    view_register_user,
    initiate_payment,
    stk_success,
    view_login_user,
    view_update_user_phone_number,
    view_logout_user,
    view_all_payments,
)


urlpatterns = [
    path("", view_login_user, name="sign-in"),
    path("sign-up/", view_register_user, name="sign-up"),
    path("sign-out/", view_logout_user, name="sign-out"),
    path("update-user-phone/", view_update_user_phone_number, name="update-phone"),
    path("initiate-stk-push/", initiate_payment, name="initiate-payment"),
    path("stk-results/", stk_push_results, name="stk-results"),
    path("success/<int:payment_id>/", stk_success, name="success"),
    path("dashboard/", view_all_payments, name="dashboard"),
]
