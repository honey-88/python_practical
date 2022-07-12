#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

from tokenize import Number


number = int(input("enter a number :"))
if number%2==0:
    print("even number")
else:
    print("odd number")
