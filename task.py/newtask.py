from asyncore import loop


students = {}

role_continue = True

while role_continue:
    roles = """
        Press-1 for Counseller
        Press-2 for Faculty
        Press-3 for Student
        -----------------------------------
    """
    print(roles)
    role_choice = int(input("\tEnter your choice for role : "))

    counseller_continue = True
    if role_choice == 1:
        while counseller_continue:
            operations = ["\n\n\t1. Add student", "\t2. Remove student", "\t3. View all student", "\t4. View specific student", "\t5. Assign new faculty to specific student", "\t---------------------------------------------"]
            for operation in operations:
                print(operation)
            operation_choice = int(input("\n\tEnter your choice for operation : "))

            if operation_choice == 1:
                student = {}
                print("\n\n\n\n\t---------------- Get Student Data ----------------")
                sr_no = int(input("\n\tEnter student serial-no. : "))
                firstname = input("\tEnter student's firstname : ")
                lastname = input("\tEnter student's lastname : ")
                contact = input("\tEnter student's contact no. : ")
                subjectname = input("\tEnter student's subjects' name seperated with space : ")
                subjectfees = input("\tEnter student's subjects' fees seperated with space : ")
                faculty = input("\tEnter faculty names' for each subject seperated with space : ")
                subjectsname = subjectname.split()
                subjectsfees = subjectfees.split()
                faculties = faculty.split()
                student_subjects = {}
                for index,subject in enumerate(subjectsname):
                    student_subjects[subject] = [subjectsfees[int(index)], faculties[int(index)]]

                # adding data to students dictionary
                student['firstname'] = firstname
                student['lastname'] = lastname
                student['contact'] = contact
                student['student_subjects'] = student_subjects
                students[sr_no] = student

                print(f"\n\t************ Students Data ************\n\t{students}")
            elif operation_choice == 2:
                print(f"\n\t************ Students Data ************\n\t{students}")
                del_ser_no = int(input("\n\n\tEnter serial-no of student you wanna delete : "))
                del students[del_ser_no]
                print(f"\n\t************ Students Data ************\n\t{students}")
            elif operation_choice == 3:
                print(f"\n\t************ Students Data ************\n\t{students}")
            elif operation_choice == 4:
                student_sr_no = int(input("\n\tEnter sr-no for student you wanna see data of : "))
                print(f"\n\t{students[student_sr_no]}")
            elif operation_choice == 5:
                assign_student = input("\n\tEnter student sr-no to assign faculty to : ")
                assign_subject = input("\tEnter subject to which you want to assign facutly to : ")
                assign_faculty = input("\tEnter faculty you want to assign to above student : ")

                students[assign_student][assign_subject] = assign_faculty
                print(f"\n\t************ Students Data ************\n\t{students}")
            else:
                print("\n\t######################################################\n\t\t\tENTER VALID OPERATION CHOICE\n\t######################################################")
            
            if(input("\n\tWant to perform some other operations? Press 'y' for yes and 'n' for no : ") == 'n'):
                break

    elif role_choice == 2:
        faculty_continue = True
        while faculty_continue:
            operations = ["\n\n\t1. Add marks to student", "\t2. View all student"]
            for operation in operations:
                print(operation)
            operation_choice = int(input("\n\tEnter choice for operation you wanna perform : "))

            if operation_choice == 1:
                assign_student = input("\n\tEnter student sr-no to assign faculty to : ")
                assign_subject = input("\tEnter subject to which you want to assign facutly to : ")
                assign_marks = int(input("\tEnter marks for above given subject : "))
                students[assign_student][assign_subject].append(assign_marks)
            elif operation_choice == 2:
                print(f"\n\t************ Students Data ************\n\t{students}")        
            else:
                print("\n\t######################################################\n\t\t\tENTER VALID OPERATION CHOICE\n\t######################################################")    
            
            if(input("\n\tWant to perform some other operations? Press 'y' for yes and 'n' for no : ") == 'n'):
                break
    elif role_choice == 3:
        student_continue = True
        while student_continue:
            operations = ["\t1. View own Details", "\t2. Pay Fees"]
            for operation in operations:
                print(operation)
            operation_choice = int(input("Enter your choice for operation to perform : "))
            if operation_choice == 1:
                sr_no = int(input("Enter your sr-no. : "))
                print(students[sr_no])
            elif operation_choice == 2:
                sr_no = int(input("Enter your sr-no. : "))
                fees_amount = int(input("Enter amount of fees you want to pay : "))
                students[sr_no]["fees_paid"] = fees_amount
            else:
                print("\n\t######################################################\n\t\t\tENTER VALID OPERATION CHOICE\n\t######################################################")    
            
            if(input("\n\tWant to perform some other operations? Press 'y' for yes and 'n' for no : ") == 'n'):
                break
    else:
        print("\n\t######################################################\n\t\t\tENTER VALID ROLE CHOICE\n\t######################################################")

    if(input("\n\tWanna continue running this application? Press 'y' for yes and 'n' for no : ") == 'n'):
        break