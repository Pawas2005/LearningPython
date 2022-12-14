# WAP to declare a private data member name for class employee

class Employee:
    __name = "Anu"
    empid = 11111
    _department = "CSE"

    def display(self):
        print(self.empid)
        print(self.__name)
        print(self._department)


e1 = Employee()
e1.display()
