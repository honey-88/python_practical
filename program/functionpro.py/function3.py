from secrets import choice


def menu():
    data = """
                    MENU
            press 1 for addition 
            press 2 for multiplication
    
            """
    print(data)
    choice = int(input("enter your choice : "))
    if choice==1:
        addition()
    elif choice==2:
        mul()

def addition():
    num1 = int(input("enter number 1 : "))
    num2 = int(input("enter number 2 : "))
    ans = num1 + num2
    print(ans)

def mul():
    num1 = int(input("enter number 1 : "))
    num2 = int(input("enter number 2 : "))
    ans = num1 * num2
    print(ans)

status = True
while status:
    menu()
    choice = input("do you want to continue press 'y' for yes and press 'n' for no: ")
    if choice=='n' or choice=='no':
        status = False