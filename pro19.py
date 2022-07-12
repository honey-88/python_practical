#number between 10 to 50 ot 51 to 100.

num = int(input("enter a num: "))

if num>10 and num<50:
    print("number is between 10-50")
elif num>51 and num<100:
    print("number is between 51-100")
else:
    print("number is beolw 10 or number is above 100")