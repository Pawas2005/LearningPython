# WAP to create a base class which initialise instance variable a=5
# return using function and the function name is get_value
# now create a derived class get_value which increments the value of variable a from base class

class Base:
    def __init__(self):
        self.a = 5  # instance variable

    def get_value(self):
        return self.a


class Derived(Base):
    def get_value(self):
        return self.a + 4


O1 = Derived()
print(O1.get_value())
