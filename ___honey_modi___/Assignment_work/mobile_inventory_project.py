mobile_store={}
customer_cart={}

menu= """
                MENU

            press 1 for product manager
            press 2 for customer
        """

status = True
while status:
    specification = {}
    print(menu)
    role = int(input("choose your role(1/2) :"))
    if role == 1:
        print("product manager")

        product_name = input("enter product_name:")

        model_num = input("enter model number: ")
        color = input("enter color name :")
        qty = int(input("enter qty :"))
        price = int(input("enter price :"))

        specification["model"] = model_num
        specification["color"] = color
        specification["qty"] = qty
        specification["price"] = price

        mobile_store[product_name] = specification

        print(mobile_store)
    elif role==2:
        print("custmore")

        product_name = input("enter product_name :")

        model_num = input("enter model number: ")
        color = input("enter color name :")
        qty = int(input("enter qty :"))
        price = 20500
        total  = price * qty
        print(total)
        
        specification["model"] = model_num
        specification["color"] = color
        specification["qty"] = qty
        

        customer_cart[product_name] = specification

        print(customer_cart)

    else:
        print("Invalid input")

    choice = input("do you want to continue: press 'y' for yes and press 'n' for no: ")
    if choice=='n' or choice=='no':
        status= False

for k in mobile_store.keys():
    print("---------------------")
    print(f"PRODUCT:{k}")
    print("MODEL: "+mobile_store[k]["model"])
    print("color :"+mobile_store[k]["color"])
    print("qty :" +str(mobile_store[k]["qty"]))
    print("price : "+str(mobile_store[k]["price"]))

