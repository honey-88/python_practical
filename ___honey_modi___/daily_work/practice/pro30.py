#accept 5 numbers find count no.of even and no.of odds.

even_count = 0
odd_count = 0
for i in range(1,6):
    num = int(input("enter a number: "))
    print("num =",num)
if num%2==0:
    even_count +=1
else:
    odd_count +=1

print("even_count =",even_count)
print("odd_count =",odd_count)