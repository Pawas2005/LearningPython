# WAP to declare a class 1 with class attribute x and print that value using function 1
# declare a class 2 with class attribute y and print that value using function 2
# then declare a class 3 which derives features of class 2 and function 3 will add the contents of class 1 attributes
# class 2 attributes and class 3 attributes
# access all features using object declare for class 3

class One:
    x = 20

    def fun1(self):
        print(self.x)


class Two(One):
    y = 30

    def fun2(self):
        print(self.y)


class Three(Two):
    z = 40

    def fun3(self):
        print(One.x + Two.y + self.z)


O1 = Three()
O1.fun1()
O1.fun2()
O1.fun3()
