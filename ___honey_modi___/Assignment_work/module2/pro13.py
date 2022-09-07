#Write a Python program to get the Fibonacci series of given range.

# 0 1 1 2 3 

from itertools import count


n1=0
n2=1

limit = int(input("enter a number :"))
print(n1)
print(n2)

count=2
while count<limit:
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3)
    count+=1