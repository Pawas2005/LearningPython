# WAP to declare a base class A with init constructor
# Declare Derived class B with init constructor and access details of parents class using child class object

class A:
    def __init__(self):
        print("Parent Constructor")


class B(A):
    def __init__(self):
        A.__init__(self)
        print("Child Constructor")


O1 = B()
