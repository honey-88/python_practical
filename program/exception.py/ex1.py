try:
    num1 = int(input("enter a number : "))
    num2 = int(input("enter a number  : "))

    ans = num1/num2

 
    print(ans)
except ZeroDivisionError:
    print("make sure entered number is greater than 0 ")
except:
    print("invalid input")
else:
    print(ans)
finally:
    print("THANK YOU FOR USING THIS APP")