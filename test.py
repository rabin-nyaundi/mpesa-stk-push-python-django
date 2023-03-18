import uuid
from enum import Enum
import datetime
import base64

import requests
from requests.auth import HTTPBasicAuth
from mpesa_stk_push.settings import MPESA_SHORTCODE, CONSUMER_KEY, CONSUMER_SECRET, MPESA_PASSKEY, MPESA_API_ENDPOINT


class PaymentStatus(str, Enum):
    INITIATING = "INITIATING"
    PENDING = "PENDING"
    CANCELED = "CANCELED"
    SUCCESS = "SUCCESS"


PAYMENT_STATUS = [
    ("INITIATING", "INITIATING"),
    ("CREATED", "CREATED"),
    ("SETTLED", "SETTLED"),
    ("SUSPENSE", "SUSPENSE"),
    ("FAILED", "FAILED"),
]


# for i in PaymentStatus:
#     print(i)
#     print(type(PaymentStatus))
# print([PaymentStatus])
# print(type(PAYMENT_STATUS))


# def convert(date_time):
#     format = "%b %d %Y %I:%M%p"  # The format
#     datetime_str = datetime.strptime(date_time, format)

#     return datetime_str


# # Driver code
# date_time = "20230315133909"
# print(convert(date_time))


def __get_access_token():
    auth_url = f"{MPESA_API_ENDPOINT}oauth/v1/generate?grant_type=client_credentials"
    print(auth_url)

    string_to_encode = CONSUMER_KEY + CONSUMER_SECRET

    sample = string_to_encode.encode("ascii")
    base64_bytes = base64.b64encode(sample)
    base64string = base64_bytes.decode("ascii")

    print(base64string)

    access_token = None

    if not access_token:
        response = requests.get(auth_url, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
        print(response.text)
        auth_json = response.json()
        print(access_token)
        access_token = auth_json.get("access_token")

        return access_token


__get_access_token()
