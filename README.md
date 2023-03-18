# MPESA STK PUSH - PYTHON DJANGO

The project has an admin dashboard that you can view all the payments, their statuses whether successfull of failed.

To Set up the project clone or fork the repository
```bash 
git clone https://github.com/mpesa-stk-push-python-django

```
Set up the environment variables.

Inside the project directory locate the ```settings.py``` file.

In the same directory, create an env file ```.env```.
```bash 
.env


SECRET_KEY=<secret_key> # your secret key

MPESA_PASSKEY=<Mpesa passkey>  # obtained from Mpesa daraja Portal

MPESA_BUSINESS_NUMBER=12345 # Business Number provided by MPESA DARAJA API for testing

MPESA_SHORTCODE=174379  #Shortcode also provided by MPESA DARAJA API for testing

CONSUMER_KEY=<consumer_key> # consumer key provided by MPESA DARAJA API for testing

CONSUMER_SECRET=<consumer_secret>    #consumer secret also provided by MPESA DARAJA API for testing

MPESA_API_ENDPOINT=https://sandbox.safaricom.co.ke/ 

MPESA_CALLBACK_URL=<callback_url> # for localhost testing you cMPESA DARAJA API for testingan set ngrok

```
Create virtual environment
```bash 
python3 -m venv <name_of_your_virtualenvirnment>
```

Install dependencies.

To install the dependencies, navigate to project root directory and open terminal.
```bash
pip install -r requirements.txt
```

Run the Migrations.

You can set your own database. For this project we are using ```sqlite```
```bash 
python3 manage.py migrate
```

The finnaly run the server.

```bash
python3 manage.py runserver
```

Create a super user or admin user with email and password.

Admin user can view all the payments when logged in to the application.

```bash
python3 manage.py createsuperuer
```

Visit ```http://localhost:8000/``` to view on the browser.
```bash
http://localhost:8000/
```

Register a user on regiter user page.

Login then make payment form your safaricom phone.

Logout and login again as a ```superuser``` or ```admin``` to view the payment list.

