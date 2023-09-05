class Student:
    student_id = '0000'
    name = ''
    phone_no = ''

    def __init__(self, sid = '', name = '', phoneNo =''):
        self.student_id = sid
        self.name = name
        self.phone_no = phoneNo

    def __str__(self):
        return 'Name:'+ self.name+ ' | ID:'+self.student_id

    def learn(self):
        print("Ok, Alright... I am studying...")

    def changePhoneNo(self, newPhoneNo):
        self.phone_no = newPhoneNo
        print("The phone number changed to ", newPhoneNo)

class Document:
    title = ''
    author = ''
    date = ''
    body = ''
    id = ''

    def __init__(self, title = '', author = '', date = '', body = '', id = ''):
        self.title = title
        self.author = author
        self.date = date
        self.body = body
        self.id = id

    def __str__(self):
        return 'Title:'+ self.title+ ' | Author:'+self.author

    def printDoc(self):
        print("The document was sent to the printer")

    def emailDoc(self):
        email = input()
        print("The document was emailed to: ", email)


