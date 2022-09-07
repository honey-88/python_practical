#write a python program to get the factorial number of given number.

n = input("enter a number :")
factorial = 1
if int(n)>=1:
    for i in range(1,int(n)+1):
        factorial = factorial*i
    print("factorial of",n,"is:",factorial)

