
#Write a Python program to find the highest 3 values in a dictionary
d = {"a": 1, "b": 2, "c": 3,"d":4,"e":5}
max_key = max(d, key=d.get)
print(max_key)

#output : e