#Write a Python program to unzip a list of tuples into individual lists.
l = [(1,2),(2,3),(3,4)]
print(list(zip(*l)))


#zip function returns the zip object , it is a
#iterator of tuples which passes the first item  in paired

#output: [(1, 2, 3), (2, 3, 4)]
