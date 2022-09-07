
from secrets import choice


menu = """
                SELECT YOUR ROLE
                press 1 for doctor
                press 2 for patient


        """
print(menu)

choice = ("select your role 1/2 : ")

class user: 
    def __init__(self):
        print("user class")

    def input(self):
        self.email = input("enter email: ")
        self.password = input("enter password : ")

class doctor(user):
    def doc_input(self):
        self.specification = input("enter specification: ")

class patent(doctor):
    def pat_input(self):
        self.email = input("enter email : ")
        self.password = input("enter password : ")

    def display(self):
        print("doctor email = ",self.email)
        print("doctor password = ",self.password)
        print("doctor specification = ",self.specification)

if choice == 1:
    doctor_obj = doctor()   
    doctor_obj.input()
    doctor_obj.doc_input()  
    doctor_obj.display()

else:

   patient_obj = patient()
   patient_obj.input()
   patient_obj.pat_input()
   patient_obj.display()