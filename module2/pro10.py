#Write a Python program to count the number of characters (character frequency) in a string

from itertools import count


name =input("enter a name :")
count=0
for i in name:
    count+=1
    print(i)

print(count)