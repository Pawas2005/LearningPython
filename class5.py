# WAP to create a class with student
# Take the input from the user for name and age
# Name and age attributes initialised as arguments within __init__ method body


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


n1 = input("Enter name ")
n2 = int(input("Enter age "))
O1 = Student(n1, n2)
print(O1.name, O1.age)
