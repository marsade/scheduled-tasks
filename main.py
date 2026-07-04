#!/usr/bin/env python3
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import smtplib
import random


birthdays = pandas.read_csv("birthdays.csv")
today = dt.date.today()


def send_mail(to_email, msg):
    mail = os.environ.get("MY_EMAIL")
    password = os.environ.get("MY_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(
            from_addr=mail,
            to_addrs=to_email,
            msg=f"Subject:Happy Birthday!\n\n{msg}"
        )


letter = ["letter_templates/letter_1.txt",
          "letter_templates/letter_2.txt",
          "letter_templates/letter_3.txt"]
letter_choice = random.choice(letter)

for (_, row) in birthdays.iterrows():
    bdate = dt.date(row["year"], row["month"], row["day"])
    if bdate == today:
        with open(letter_choice) as f:
            c = f.read()
            letter = c.replace("[NAME]", row["name"])
            send_mail(row["email"], letter)
