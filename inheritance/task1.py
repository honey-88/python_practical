status = True
while status:

    data = """
                    select your role

                    press 1 for doctor
                    press 2 for patient
       
           """
print(data)


if choice == 1:
    print("enter doctor  email :")
    print("enter doctor password  :")
    print("enter  doctor specification:")

elif choice == 2:
    print("enter patient email : ")
    print("enter ptient password : ")

else:
    print("invaild input " )

status = False
