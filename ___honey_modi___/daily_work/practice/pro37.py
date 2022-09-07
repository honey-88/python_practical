# function with parameter and without using return type.

from ast import Num
from re import S


def sum (num1,num2):
    print(num1)
    print(num2)

    ans = num1 + num2
    print(ans)
 
num1 = int(input("enter a num1 : "))
num2 = int(input("enter a num2 : "))


sum(num1,num2)

