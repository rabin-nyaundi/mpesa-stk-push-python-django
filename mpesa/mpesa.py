import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

from mpesa_stk_push.settings import MPESA_SHORTCODE, CONSUMER_KEY, CONSUMER_SECRET, MPESA_PASSKEY, MPESA_API_ENDPOINT


class MpesaAPI:
    def __init__(self):
        self.consumer_key = CONSUMER_KEY
        self.consumer_secret = CONSUMER_SECRET
        self.mpesa_shortcode = MPESA_SHORTCODE
        self.pass_key = MPESA_PASSKEY
        self.mpesa_endpoint = MPESA_API_ENDPOINT
        self.access_token = None

    def __get_access_token(self):
        auth_url = f"{self.mpesa_endpoint}oauth/v1/generate?grant_type=client_credentials"

        if not self.access_token:
            response = requests.get(auth_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
            auth_json = response.json()
            self.access_token = auth_json.get("access_token")
            return self.access_token

    def __generate_mpesa_password(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        data_to_encode = self.mpesa_shortcode + self.pass_key + timestamp
        online_password = base64.b64encode(data_to_encode.encode())
        password = online_password.decode("utf-8")

        return password, timestamp

    def initiate_stk_push(self, phone_number, amount, callback_url):
        cleaned_pnone_nmber = f"254{phone_number[1:]}"
        print(cleaned_pnone_nmber)

        access_token = self.__get_access_token()
        password, timestamp = self.__generate_mpesa_password()
        stk_push_url = f"{self.mpesa_endpoint}mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
        payload = {
            "BusinessShortCode": self.mpesa_shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": cleaned_pnone_nmber,
            "PartyB": "174379",
            "PhoneNumber": cleaned_pnone_nmber,
            "CallBackURL": callback_url,
            "AccountReference": "Test Company",
            "TransactionDesc": "Payment for services",
        }
        stk_push_response = requests.post(stk_push_url, headers=headers, json=payload)
        return stk_push_response.json()
