# WAP to declare object of derived class with class perimeter name, roll no, branch and age
# name, roll no and branch is instance object of parent class
# age is instance object of child class
# display contents of student details with derived class objects only

class A:
    def __init__(self, name, rollno, branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch


class B(A):
    def __init__(self, name, rollno, branch, age):
        self.age = age
        A.__init__(self, name, rollno, branch)
        print(self.name, self.rollno, self.branch, self.age)


O1 = B("Rohit", 30, "CSE", 19)
