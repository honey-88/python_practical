#Write a Python program to get unique values from a list


import random
unique_num = []
count = 0
while count<12:
    num = random.randint(1,100)
    if num not in unique_num:
            unique_num.append(num)
    count+=1
        
        
print(unique_num)