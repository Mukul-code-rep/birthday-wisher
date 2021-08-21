import smtplib
import datetime as dt
import pandas as pd
import random
import os

birthday_cards = ['letter_templates/letter_1.txt',
                  'letter_templates/letter_2.txt',
                  'letter_templates/letter_3.txt']

my_email = os.environ.get("email")
password = os.environ.get("password")

data = pd.read_csv('birthdays.csv')
months = data['month'].to_list()
days = data['day'].to_list()

now = dt.datetime.now()

for i in range(len(months)):
    if months[i] == now.month and days[i] == now.day:
        temp_choice = random.choice(birthday_cards)
        with open(temp_choice) as f:
            wish = f.read()
        wish = wish.replace('[NAME]', data['name'][i])
        with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=data['email'][i],
                                msg=f'Subject:Happy Birthday\n\n{wish}')