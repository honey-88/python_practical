#Write a Python program to read first n lines of a file.


f = open("C:\Users\Honey\Documents\GitHub\python_practical\___honey_modi___\Assignment_work\example.txt","a")
print(f.readline())
#readline : read the first line it will display one - one line

l1 = f.readlines()

print("------>",l1)
print("no.of lines in file:",len(l1))

print("3rd line of file",l1[1])