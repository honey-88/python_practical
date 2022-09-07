#Write a Python program to remove an empty tuple(s) from a list of tuples.
l = [(''),(''),('10'),('20')]
l = [ t for t in l if t]
print(l)