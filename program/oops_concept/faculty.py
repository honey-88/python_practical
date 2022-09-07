class Facultyclass:
    name = ""
    email = ""
    number = ""
    subject = ""
    city = " "

    
    dict = {}

    def createFaculty(self,firstname,email,contact,subject,city):
        innerDict = {}
        self.name = firstname
        self.email = email
        self.subject = subject
        self.number = contact
        self.city = city


        innerDict['email'] = self.email
        innerDict['subject'] = self.subject
        innerDict['number'] = self.number
        innerDict['city'] = self.city

        self.dict["firstname"] = innerDict

        print(self.dict)

        