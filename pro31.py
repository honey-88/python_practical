#accept 5 numbers from user and count no of positive number and negative.

positive_count = 0
negative_count = 0
 
for i in range (1,6):
    num = int(input("enter a number: "))
    print("num = ",num)

if num>=0:
    positive_count +=1
else:
    negative_count +=1
print("positive_count =",positive_count)
print("negative_count =",negative_count)