#jay_bhavani

product = []
qty_list = []
price = []
data= """
                            WELCOME TO JAY BHAVANI

                        VADAPAV 30
                        DABELI 30
                        BHEL 70
"""
print(data)
for i in range(1,3):
    product_name = input("enter you product:").upper()
    qty = int(input("enter no. of qty do you want:"))
    if product_name=="VADAPAV" or product_name=="DABELI":
        price_value = 30
        total_price = price_value * qty

    product.append(product_name)
    qty_list.append(qty)
    price.append(total_price)

for i in range (0,len(product)):
    print(f"{product[i]} {qty_list[i]} = {price[i]}")

print("--------------REMOVE PRODUCT----------------")
product_name = input("enter product which you want to remove:").upper()
position = product.index(product_name)

product.pop(position)
qty_list.pop(position)
price.pop(position)

for i in range(0,len(product)):
        print(f"{product[i]} {qty_list[i]} = {price[i]}")



