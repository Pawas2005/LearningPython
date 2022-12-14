# WAP to create a class furniture with function print details
# Create a child class chair which is also creating print detail function

class Furniture:
    def printdetails(self):
        print("Parent class detail")


class Chair(Furniture):
    def printdetails(self):
        print("Child")

O1 = Chair()
O1.printdetails()
O2 = Furniture()
O2.printdetails()
