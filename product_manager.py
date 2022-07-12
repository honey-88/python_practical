#product manager 

fruits = {} #blank dictionary

menu = """
            press 1 for add fruits
            press 2 for view fruits
            press 3 for purchse fruits
            press 4 for exit

        """

status = True
while status:
    print(menu)
    specification  = {}
    choice = int(input("enter you choice :"))
    if choice == 1:
        fruit_name = input("enter your choice : ")
        qty = int(input("enter qty of fruits :"))
        price = int(input("enter price : "))

        specification['qty'] = qty
        specification['price'] = price

        fruits[fruit_name] = specification

    elif choice == 2:
        for k in fruits.keys():
            print("----------------------")
            print(f"fruit name : {k} ")
            print(f"fruit qty : ",fruits[k]["qty"])
            print(f"fruit price : {k} ",fruits[k]["price"])
    elif choice == 3:
        for k in fruits.keys():
            print("----------------------")
            print(f"fruit name : {k} ")
            print(f"fruit price : (for 1 piece) ",fruits[k]["price"])

        fruit_name = input("enter fruit which you want to purchse : ")
        if fruit_name in fruits.keys():
            qty = int(input("enter no. qty you want : "))

            price = qty * fruits[fruit_name]['price']
            print("PRICE =",price)

    elif choice ==4:
        status = False
        break
    user_choice = input("do you want to continue press 'y' for yes and press 'n' for no : ")
    if user_choice == 'n':
        status= False
    else:
        status= True
