#give a number by user.
#factorial number.

num = int(input("enter a number: "))
if num>0:
    f = 1
    for i in range(1,num+1):
        f*=i
        print("factorial =",f)
else:
    print("invalid input")