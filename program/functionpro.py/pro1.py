#function without parameters and function with return type.

import re
from unittest import result


def sum():
    num1 = int(input("enter number 1 : "))
    num2 = int(input("enter number 2 : "))

    ans = num1 + num2

    return ans

result = sum()
print(result)