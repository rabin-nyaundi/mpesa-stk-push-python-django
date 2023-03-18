# MPESA STK PUSH - PYTHON DJANGO
## Project Setup

MPESA stk-push intergration with dashboard to enable admin/supersuer to view all payments made. 

The project uses Tailwindcss for styling the web pages, 

1. To Set up the project clone or fork the repository
    ```sh 
    git clone <repo>
    ```
2. Set up the environment variables.

    - Inside the project directory locate the ```settings.py``` file.

    - In the same directory as `settings.py`, create an env file ```.env```.
    ```sh 
    .env

    SECRET_KEY=<secret_key> # your secret key
    MPESA_PASSKEY=<Mpesa passkey>  # obtained from Mpesa daraja Portal
    MPESA_BUSINESS_NUMBER=12345 # Business Number provided by MPESA DARAJA API for testing
    MPESA_SHORTCODE=174379  #Shortcode also provided by MPESA DARAJA API for testing
    CONSUMER_KEY=<consumer_key> # consumer key provided by MPESA DARAJA API for testing
    CONSUMER_SECRET=<consumer_secret>    #consumer secret also provided by MPESA DARAJA API for testing
    MPESA_API_ENDPOINT=https://sandbox.safaricom.co.ke/ 
    MPESA_CALLBACK_URL=<callback_url> # for localhost you can use ngrok
    ```

3. Create virtual environment
    ```sh 
    python3 -m venv <name_of_your_virtualenvirnment>
    ```

4. Install dependencies.

    - To install the dependencies, navigate to project root directory and open terminal.
    
    ```sh
    pip install -r requirements.txt
    ```

5. Run the Migrations.

   - You can set your own database. For this project we are using ```sqlite```
    ```sh 
    python3 manage.py migrate
    ```

6. The finnaly run the server.

    ```sh
    npm run tailwind-watch
    
    python3 manage.py runserver
    ```

7. Create a super user or admin user with email and password.

   - Admin user can view all the payments when logged in to the application.

    ```sh
    python3 manage.py createsuperuer
    ```

8. Visit ```http://localhost:8000/``` to view on the browser.
    ```sh
    http://localhost:8000/
    ```

   - Register a user on regiter user page.

   - Login then make payment form your safaricom phone.

   - Logout and login again as a ```superuser``` or ```admin``` to view the payment list.

