# WAP to create a class value added courses
# Take inputs from user for course name, course credits and branch
# Print the details with function display
# Inherit new course from base class, reading a new name from user
# Declare a private variable in new class, name is practicals and print all the details using new class object

class Value_Added_Courses:
    cname = input()
    ccredits = input()
    branch = input()

    def display(self):
        print(self.cname, self.ccredits, self.branch, "(Parent Class)")


class Course(Value_Added_Courses):
    __practicals = input()

    def display2(self):
        print(Value_Added_Courses.cname, Value_Added_Courses.ccredits, Value_Added_Courses.branch, self.__practicals,
              "(Child class)")


O1 = Course()
O1.display()
O1.display2()
