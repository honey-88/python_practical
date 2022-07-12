#email or password

import email


email = "a@gmail.com"
password = "12345"

s_email = input("enter email: ")
s_password = input("enter password: ")

if s_email==email:
    if s_password==password:
        print("welcome to tops technologies")
    else:
        print("invaild password")
else:
        print("invalid email")