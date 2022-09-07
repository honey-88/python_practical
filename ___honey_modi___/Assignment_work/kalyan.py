#kalyan jewellers

name = input("Enter a name:")
contact_num = int(input("Enter a contact number:"))
customer_gender = input("Enter gender:")
customer_age = int(input("Enter age:"))
Product_name = input("enter a product name:")
product_quantity = float(input("enter product quantity:"))
current_price = 4829
making_charge = 589
price_quality = (current_price*product_quantity)

#purchase amount.
if product_quantity >=10:
    making_charge2 = (589*product_quantity)/100
    purchase_amount = price_quality*making_charge
    print("total amount:", purchase_amount)
else:
    print("total price:", price_quality+making_charge)

#senior citizen discount
if customer_age>=60:
    print("senior")
elif customer_gender == 'M' and purchase_amount>200000:
    total = (purchase_amount*10)/100
    purchase_amount -=total
    print("total price:",total)

elif customer_gender == 'M' and purchase_amount>500000:
    total = (purchase_amount*15)/100
    purchase_amount -=total
    print("total price:",total)
elif customer_gender == 'M' and purchase_amount>1000000:
    total = (purchase_amount*20)/100
    purchase_amount -=total
    print("total price", total)
elif customer_gender == 'F' and purchase_amount>200000:
    total = (purchase_amount*15)/100
    purchase_amount -=total
    print("total price:",total)
elif customer_gender == 'F' and purchase_amount>500000:
    total = (purchase_amount*20)/100
    purchase_amount -=total
    print("total price:",total)
elif customer_gender == 'F' and purchase_amount>1000000:
    total = (purchase_amount*25)/100
    purchase_amount -=total
    print("total price:",total)
else:
    if customer_gender == 'M' and purchase_amount>200000:
        total = (purchase_amount*5)/100
        purchase_amount -=total
        print("total price:",total)

    elif customer_gender == 'M' and purchase_amount>500000:
        total = (purchase_amount*10)/100
        purchase_amount -=total
        print("total price:",total)

    elif customer_gender == 'M' and purchase_amount>1000000:
        total = (purchase_amount*15)/100
        purchase_amount -=total
        print("total price:",total)

    elif customer_gender == 'f' and purchase_amount>200000:
        total = (purchase_amount*10)/100
        purchase_amount -=total
        print("total price:",total)

    elif customer_gender == 'f' and purchase_amount>500000:
        total = (purchase_amount*15)/100
        purchase_amount -=total
        print("total price:",total)

    elif customer_gender == 'f' and purchase_amount>1000000:
        total = (purchase_amount*20)/100
        purchase_amount -=total
        print("total price:",total)
        

   
