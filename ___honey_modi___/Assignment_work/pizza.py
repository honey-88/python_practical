#pizza

pizza = {}
pizza_store = {}
product = []
qty_list = []
price = []
Menu = """
            Welcome to Amazing Pizza and Pasta Pizzeria
            press 1 for order menu
            press 2 for exit 
        """
status = True
while status:
     specification = {}
     print(Menu)
     role = int(input("enter your role(1/2) : "))
     if role == 1:
        print("order menu")


        pizza_name = input("enter pizza_name: ")
        pizza_size = input("enter pizza_size :")
        qty = int(input("enter qty :"))
        price = 350
        total  = price * qty
        print(total)

        specification["pizza_name"] = pizza_name
        specification["pizza_size"] = pizza_size
        specification["qty"] = qty
        
        pizza_store[pizza] = specification

        print(pizza_store)

else:
     print("Invalid input")

choice = input("do you want to continue: press 'y' for yes and press 'n' for no: ")
if choice=='n' or choice=='no':
     status= False

for k in pizza_store.keys():
    print("---------------------")
    print(f"PRODUCT:{k}")
    print("MODEL: "+pizza_store[k]["name"])
    print("color :"+pizza_store[k]["size"])
    print("qty :" +str(pizza_store[k]["qty"]))
    print("price : "+str(pizza_store[k]["price"]))
