from datetime import datetime
import pytz
import re


def convert_string_to_datetime(date_string: str):
    date_object = datetime.strptime(date_string, "%Y%m%d%H%M%S")
    date_tz = pytz.timezone("Africa/Nairobi")
    utc_timezone = date_tz.localize(date_object)
    return utc_timezone


# Email Regex
def validate_email(email_address: str):
    email_reggex = "^([a-z0-9.-]+)@([a-z0-9]+\.[a-z]{2,8})(\.[a-z]{2,8})?$"
    is_valid = re.match(email_reggex, email_address)
    if is_valid:
        print("Email address is valid")
    else:
        print("Email address is invalid")

    return is_valid


# validate_email("rabin-nyaundi254@gmail.com")


# Password Reggex
def validate_password(password):
    ...
