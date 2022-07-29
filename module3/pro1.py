#Write a Python function to get the largest number, smallest num and sum of all from a list

NumList = []
# Take the input from user
Number = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element: " %i))
    NumList.append(value)

# Print the List Entered by the User
print("List: ",NumList)

print("The Smallest Element in this List is: ", min(NumList))
print("The Largest Element in this List is: ", max(NumList))