name = input("Enter your name : ")
mob = input("Enter mob.no : ")
gender = input("Enter your gender : ")
age = int(input("Enter your age : "))
product_name = input("Enter product name : ")
qty = float(input("Enter quantity of your product : "))

CURRENT_PRICE = 4829.0
MAKING_CHARGES = 589.0


# def printData(name, product_name, qty, making_charges, total_charges):
#     print(f"Product : {product_name}")
#     print(f"Quantity : {qty}")
#     print(f"Making charges : {making_charges}")
#     print(f"Total amount : {total_charges}")


print("\n\n-------------------------- Invoice --------------------------")
print(f"Name : {name}")
print(f"Mobile number : {mob}")
print(f"Gender : {gender}")
print(f"Age : {age}")
print(f"Product : {product_name}")
print(f"Quantity : {qty}")
print(f"Current price : {CURRENT_PRICE}")

if qty > 10.0:
    updated_making_charges = MAKING_CHARGES + (MAKING_CHARGES * 0.1)
    total_amount = (qty * CURRENT_PRICE) + updated_making_charges
    print(f"Making charges : {updated_making_charges}")
    print(f"Purchase amount : {total_amount}")
    if gender=="male" and age >= 60:
        if total_amount > 1000000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.2
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 500000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.15
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 200000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.1
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        else:
            print("-------------------------------------------------")
            discount = total_amount*0
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
    elif gender=="male" and age < 60:
        if total_amount > 1000000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.15
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 500000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.1
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 200000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.05
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        else:
            print("-------------------------------------------------")
            discount = total_amount*0
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
    elif gender=="female" and age >= 60:
        if total_amount > 1000000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.25
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 500000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.2
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 200000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.15
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        else:
            print("-------------------------------------------------")
            discount = total_amount*0
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
    elif gender=="female" and age < 60:
        if total_amount > 1000000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.2
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 500000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.15
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 200000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.1
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        else:
            print("-------------------------------------------------")
            discount = total_amount*0
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
else:
    total_amount = (qty * CURRENT_PRICE) + MAKING_CHARGES
    print(f"Making charges : {MAKING_CHARGES}")
    print(f"Purchase amount : {total_amount}")
    if gender=="male" and age >= 60:
        if total_amount > 1000000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.2
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 500000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.15
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 200000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.1
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        else:
            print("-------------------------------------------------")
            discount = total_amount*0
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
    elif gender=="male" and age < 60:
        if total_amount > 1000000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.15
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 500000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.1
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 200000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.05
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        else:
            print("-------------------------------------------------")
            discount = total_amount*0
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
    elif gender=="female" and age >= 60:
        if total_amount > 1000000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.25
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 500000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.2
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 200000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.15
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        else:
            print("-------------------------------------------------")
            discount = total_amount*0
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
    elif gender=="female" and age < 60:
        if total_amount > 1000000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.2
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 500000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.15
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        elif total_amount > 200000.0:
            print("-------------------------------------------------")
            discount = total_amount*0.1
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")
        else:
            print("-------------------------------------------------")
            discount = total_amount*0
            print(f"Discount : {discount}")
            disamount = total_amount - discount
            print(f"Disamount : {disamount}")
            gst = disamount*0.18
            print(f"GST : {gst}")
            total_amount = disamount + gst
            print(f"Net amount : {total_amount}")