class Calculations:
    def Summations(self, a, b):
        return a + b
class Calculation2:
    def Multiplication(self, a, b):
        return a * b

class Derived(Calculations, Calculation2):
    def divide(self, a, b):
        return a/b


D = Derived()
print(D.Summations(10, 20), D.Multiplication(30, 40), D.divide(30, 10))
