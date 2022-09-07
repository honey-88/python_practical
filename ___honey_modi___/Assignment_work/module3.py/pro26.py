#Write a Python script to sort (ascending and descending) a dictionary by value.
l1 = [1,2,3,4,5,6,4,5,72,8465123]
l1.sort()
print(l1)

#output : [1, 2, 3, 4, 4, 5, 5, 6, 72, 8465123] (ascendind)

l1.sort(reverse=True)
print(l1)

#output : [8465123, 72, 6, 5, 5, 4, 4, 3, 2, 1] (descending)