#while loop

status = True
while status:
    subject = input("enter subject name  :")
    choice = input("do you want to enter more subject? press'y' for yes and press 'n' for no : ")
if choice=='n' or choice =='no' or choice=='N':
    status = False