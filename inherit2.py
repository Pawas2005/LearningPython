# WAP to create a class name student with first name, last name, and marks
# Pass these attributes at the time of object declaration
# and print these values using child object only

class student:
    def __init__(self, fname, lname, marks):
        self.fname=fname
        self.lname=lname
        self.marks=marks


    def display(self):
        print(self.fname, self.lname, self.marks)


class ch(student):
    pass


O1=ch("Suryakumar", "Yadav", 200)
O1.display()