import os
import random
import smtplib

def automated_mail():
    email = input(" enter your email:")
    name = input(" enter yoyr full name:")
    message= (f"{name}, welcome to myntra")
    s= smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("your mail","google app password")
    s.sendmail("&&&&&&&&&&&",email, message)
    print(" email sent!")

automated_mail()

