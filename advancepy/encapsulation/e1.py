class student:
    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name

    def setsubject(self,subject):
        self.subject = subject

    def getsubject(self):
        return self.subject

obj = student()
obj.setname("honey")
obj.setsubject("python")

print("name = ",obj.getname())
print("subject = ",obj.getsubject())