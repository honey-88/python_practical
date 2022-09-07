class studentclass:
    name = "hetvi"
    email = ""
    number = ""
    subject = ""
    city = " "
    fees = ""
    marks = ""

    dict = {}

    def createstudent(self,name,email,contact,subject,city,fees,marks):
        innerDict  ={}
        self.name = name
        self.email = email
        self.subject = subject
        self.number = contact
        self.city = city
        self.fees = fees
        self.marks = marks

        innerDict['email'] = self.email
        innerDict['subject'] = self.subject
        innerDict['number'] = self.number
        innerDict['city'] = self.city
        innerDict['fees'] = self.fees
        innerDict['marks'] = self.marks

        self.dict[name] = innerDict

        print(self.dict)
