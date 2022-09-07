#accept marks from student and given him appropriate grade.

num = int(input("enter a student marks: "))

if num>=70:
    print("A grade")
elif num>=60 and num<=69:
    print("B grade")
elif num>=50 and num<=59:
    print("C grade")
elif num>=40 and num<=49:
    print("D grade")
else:
    print("fail")