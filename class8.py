# WAP to get course name, contact hours as input from the user
# Print the details of courses
# You have to use default constructor __init__ for taking the values
# print those with another function display courses

class Courses:
    def __init__(self, cname, contact_hours):
        self.cname = cname
        self.Contact_hours = contact_hours

    def displaycourses(self):
        print("Course", self.cname)
        print("Contact Hours", self.Contact_hours)


i = input("Course: ")
j = int(input("Hours: "))
C1 = Courses(i, j)
C1.displaycourses()
