import faculty,student

f = faculty.Facultyclass()

s = student.studentclass()

status = True

while status:
    name = input("enter student name : ")
    subject = input("enter student subject : ")
    mobile = input("enter student mobile number : ")
    city = input("enter student city : ")
    email = input("enter student email : ")
    fees  = input("enter student fees: ")
    marks = input("enter student marks : ")

    s.createstudent(name,email,mobile,subject,city,fees,marks)

    choice = input("do you want to make details press'y'for yes and press 'n'for no : ")

    if choice == 'y':
        status = True
    else:
        status = False














































