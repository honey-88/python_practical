# Write a Python program to write a list to a file.

name = ['hetvi','honey','devarsh']

f = open(r'C:\Users\Honey\Documents\GitHub\python_practical\___honey_modi___\Assignment_work\module4\name.txt','w')
for item in name:
    f.write("%s\n" % item)
print('done')