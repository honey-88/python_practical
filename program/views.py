#this is module
#this is contain only business logics

all_laptop = {
                "dell" : 65000,
                "hp" : 45000,
                "lenovo": 25000,
}

all_mobile = {
                "sumsang":85000,
                "mi":7829,
                "vivo":25000,
}

def viewlaptop():
    print("\n LAPTOP LIST: \n")
    for k,v in all_laptop.items():
        print(f"{k} = {v}")
def viewmobile():
    for k,v in all_mobile.items():
        print(f"{k} = {v}")

def purchselaptop(laptop_name,qty):
    if laptop_name in all_laptop:
        price = all_laptop[laptop_name]
        total_price = qty * price
        print("total price =",total_price)