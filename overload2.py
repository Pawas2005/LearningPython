class A:
    def area(self, a=None, b=None):
        if a != None and b == None:
            print(a*a)
        else:
            print(a*b)


A1 = A()
A1.area(30)
A1.area(30, 50)
