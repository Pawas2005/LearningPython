# WAP to perform method overloading with single argument function, two argument function, and three argument function

class A:
    def volume(self, a=None, b=None, c=None):
        if a != None and b == None and c == None:
            print(a)
        elif a != None and b != None and c == None:
            print(a, b)
        else:
            print(a, b, c)


A1 = A()
A1.volume(30)
A1.volume(30, 50)
A1.volume(30, 50, 70)
