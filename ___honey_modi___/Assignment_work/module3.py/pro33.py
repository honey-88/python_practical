#Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200,'d':400}
from itertools import count



d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}

for k in d2:
    if k in d1:
        d2[k] = d2[k]+d1[k]

    else:
        pass
print(d2)

#output: {'a': 400, 'b': 400, 'd': 400}