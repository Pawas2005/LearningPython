# WAP to create a class person with function display which print it is a parent class
# create a child class student which inherit the features of person and the new child class is empty class

class person:
    def display(self):
        print("It is a parent class")


class student(person):
    def r1(self):
        print("This is a student class")


O1 = student()
O1.r1()
