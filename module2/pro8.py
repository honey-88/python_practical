#Write a Python program to count the number of lines in a text file.

#import os 

#f = open("r,C:\Users\HETVI\OneDrive\Documents\GitHub\python_practicals\Assignment_work\module-4\myfile.txt",'r')

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)