counsellor = {}
student = {}
ser = {}
faculty = {}

menu =  """
                press 1 for add student 
                press 2 for remove student
                
        """

status = True
while status:
        
        print(menu)
        specification  = {}
        choice = input("enter your choice : ")
        if choice == 1:
                student_name = input("enter student_name : ")
                ser.no = int(input("enter your ser.no : "))
                add_student = input("add a student_name : ")

                specification['ser.no'] = ser.no
                specification['add_student'] = add_student

                student[student_name] = specification

        elif choice == 2:
                for k in student.keys():
                        print("----------------------")
                        print(f"student name : {k} ")
                        print(f"ser.no : ",student[k]["qty"])
                        print(f"add student : {k} ",student[k]["price"])