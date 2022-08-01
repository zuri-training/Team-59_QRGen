# QrGen-Team_59


## QR Code functionalities when scanned

- Document Download
- Redirection to different web addresses

## Logic

- If the QRCode points to a URL,it will autoredirect to the url bounded to it.
- If it is intented to download a file, it will autoredirect to download file.

## Testing

After cloning the repository, using; 

                virtualenv <virtual-environment-name>
                 
Activate the virtual environment you created using;              
  
    Linux/OS: 
   
                $ source <virtual-environment-name>/Scripts/activate
              
    Windows OS:
   
                path\to\<virtual-environment-name>\Scripts\activate
  
Install the required dependencies using;

                pip install -r requirements.txt
                
Prepare the models as tables to be migrated to the database using;
                
                python manage.py makemigrations
                
Migrate the tables using;

                python manage.py migrate
                 
Create a new super user using:

                python manage.py createsuperuser
                 
Then run your server using;

                  python manage.py runserver


## About django-qr-code (qr_code)
I used this already made external package to generate a qrcode so that i focus on just what happens when the code is scanned.
I won't advice us to use this package because it defeats the goal of our project as this is an already made qr code generator.
Checkout https://django-qr-code.readthedocs.io/en/latest/ for more info on qr_code
