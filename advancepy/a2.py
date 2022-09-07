#self: which is represent current class properties.

class student:
    def display(self,fname,lname):
        print("hello")
        print("fname = ",fname)
        print("lname = ",lname)

obj = student()
obj.display("honey","modi")