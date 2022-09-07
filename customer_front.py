from secrets import choice
from views import*

name = input("enter your name : ")
menu = """
                MENU
            1)laptop
            2)mobile
       
       """
print(menu)

choice = int(input("enter your choice: "))
if choice == 1:
    viewlaptop()
    laptop_name = input("enter laptop name which you want to purchse: ")
    qty = int(input("enter no.of qty do you want to purchse : "))
    total_price = purchselaptop(laptop_name,qty)

    

elif choice == 2:
    viewmobile()
else:
    print("invalid input")
