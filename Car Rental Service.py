import smtplib
from fpdf import FPDF
import random
from datetime import datetime
from gtts import gTTS
import playsound
from tkinter import *
from tkinter.ttk import *

#tts = gTTS(text='Hello Welcome to Gears Car Rental Service, Please Pick an Option To begin the rental process', lang='en')
#tts.save("greeting.mp3")

#playsound.playsound("greeting.mp3",True)

name = f'{str(random.randint(1,1000))}.pdf'
twowheeler = ['Motor Bike', 'Road Bicycle', 'Mountain Bike' ]
fourwheeler = ['4 Door Salon Car', '2 Door Salon Car', 'Pickup Truck', 'SUV', 'Van']
eighteenwheeler = ['Mercedes Eighteen Wheeler', 'MAN Eighteen Wheeler', 'ISUZU Eighteen Wheeler']

def two_wheeler(twowheeler):

    print('These are your options:')
    print('1.) Motor Bike 60 AED    | Per Day')
    print('2.) Road Bike 30 AED     | Per Day')
    print('3.) Mountain Bike 30 AED | Per Day')

    print('Press Enter 1 Time to return to Home Page')
    selectiontwo = input('Enter Option Number:\n')

    if selectiontwo == '1':
        daystwo = int(input('How many days would you like to rent the Motor Bike:\n'))
        print('Final Price:')
        print(f'{65*daystwo}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')

        print('You are All Set, Purchase Successful')
        print('Thank You for Choosing Gears Rental Service, You can pick up your Motor Bike at our Barsha Outlet')
        today = datetime.now()
        new_date = datetime.strftime(today, '%d-%b-%Y')
        print(f'Order Placed on {new_date}')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Times', 'B', 12)
        pdf.set_fill_color(0, 0, 0)
        pdf.rect(0, 0, 0, 0, 'F')

        message = f'''Dear Customer, You have rented a Motor Bike for {daystwo} days and your final price is {65*daystwo} AED, 
you can pick up your motor bike at out barsha outlet and can reverse the transaction if necessary'''


        pdf.image('PCR_Service.jpg',35,5,w=150,h=101)
        pdf.set_text_color(255, 0, 0)
        pdf.multi_cell(0, 5, message)
        pdf.ln()

        pdf.add_page()
        pdf.cell(0, 5, "Thank You for renting with Gears")
        pdf.output(name, 'F')

    elif selectiontwo == '2':
        daystwo = int(input('How many days would you like to rent the Road Bike:\n'))
        print('Final Price:')
        print(f'{35*daystwo}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your Road bike at our Barsha Outlet')

    elif selectiontwo == '3':
        daystwo = int(input('How many days would you like to rent the Mountain Bike:\n'))
        print('Final Price:')
        print(f'{35 * daystwo}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your Mountain Bike at our Barsha Outlet')

def four_wheeler(fourwheeler):

    print('These are your options:')
    print('1.) 4 Door Salon Car 100 AED | Per Day')
    print('2.) 2 Door Salon Car 150 AED | Per Day')
    print('3.) Pickup Truck 125 AED     | Per Day')
    print('4.) SUV 110 AED              | Per Day')
    print('5.) Van 130 AED              | Per Day')

    print('Press Enter 1 Time to return to Home Page')
    selectiontwo = input('Enter Option Number:\n')

    if selectiontwo == '1':
        daysfour = int(input('How many days would you like to rent the 4 Door Salon Car:\n'))
        print('Final Price:')
        print(f'{100 * daysfour}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your 4 Door Salon Car at our Barsha Outlet')

    if selectiontwo == '2':
        daysfour = int(input('How many days would you like to rent the 2 Door Salon Car:\n'))
        print('Final Price:')
        print(f'{150 * daysfour}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your 2 Door Salon Car at our Barsha Outlet')

    if selectiontwo == '3':
        daysfour = int(input('How many days would you like to rent the Pickup Truck:\n'))
        print('Final Price:')
        print(f'{125 * daysfour}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your Pickup Truck at our Barsha Outlet')

    if selectiontwo == '4':
        daysfour = int(input('How many days would you like to rent the SUV:\n'))
        print('Final Price:')
        print(f'{110 * daysfour}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your SUV at our Barsha Outlet')

    if selectiontwo == '5':
        daysfour = int(input('How many days would you like to rent the Van:\n'))
        print('Final Price:')
        print(f'{130 * daysfour}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your Van at our Barsha Outlet')

def eighteen_wheeler(eighteenwheeler):

    print('These are your options:')
    print('1.) Mercedes Eighteen Wheeler 200 AED | Per Day')
    print('2.) MAN Eighteen Wheeler 175 AED      | Per Day')
    print('3.) ISUZU Eighteen Wheeler 175 AED    | Per Day')

    print('Press Enter 1 Time to return to Home Page')
    selectiontwo = input('Enter Option Number:\n')

    if selectiontwo == '1':
        dayseighteen = int(input('How many days would you like to rent the Mercedes Eighteen Wheeler:\n'))
        print('Final Price:')
        print(f'{200 * dayseighteen}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your Mercedes Eighteen Wheeler at our Barsha Outlet')

    if selectiontwo == '2':
        dayseighteen = int(input('How many days would you like to rent the MAN Eighteen Wheeler:\n'))
        print('Final Price:')
        print(f'{175 * dayseighteen}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print('Thank You for Choosing Gears Rental Service, You can pick up your MAN Eighteen Wheeler at our Barsha Outlet')

    if selectiontwo == '3':
        dayseighteen = int(input('How many days would you like to rent the ISUZU Eighteen Wheeler:\n'))
        print('Final Price:')
        print(f'{175 * dayseighteen}AED | Inclusive of VAT')

        print('Pay with Credit Card only ')
        ncard = input('Please Enter Your Card Number:\n')
        scard = input('Please Enter you Security Code:\n')
        print('Your All Set, Purchase Successful')

        print(
            'Thank You for Choosing Gears Rental Service, You can pick up your ISUZU Eighteen Wheeler at our Barsha Outlet')

def email(emailid):
    gmail_user = ''
    gmail_password = ''

    sent_from = gmail_user
    to = emailid
    subject = 'Gears Car Rental Service'
    body = 'Your Car Rental Service order has been placed and confirmed you can pick it up at our barsha rental center'

    email_text = f"""From: {sent_from}  
    To: {to}  
    Subject: {subject}

    {body}
    """

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

print('Welcome to Gears Car Rental Service')
print('_' * 30)
selection = 0
while selection != 4:
    selection = int(input('''
    
    Enter Option Number
    -------------------
    1.) Rent A 2 Wheeler
    2.) Rent A 4 Wheeler
    3.) Rent An 18 Wheeler
    4.) Exit
    '''))

    if selection == 1:
        two_wheeler(twowheeler)
        emailid=input("Enter Email Address To Receive an Order Confirmation")
        email(emailid)
    if selection == 2:
        four_wheeler(fourwheeler)
        emailid = input("Enter Email Address To Receive an Order Confirmation")
        email(emailid)
    if selection == 3:
        eighteen_wheeler(fourwheeler)
        emailid = input("Enter Email Address To Receive an Order Confirmation")
        email(emailid)
    elif selection == 4:
        exit()
    else:
        print('Invalid Selection')
