# WAP to create a class student details with instance variable registration number, name and marks
# Also display these details with disp function
#


class StudentDetails:
    def __init__(self):
        self.name = "Ab"
        self.reg = "12214148"
        self.marks = 100

    def disp(self):
        print(self.name, self.reg, self.marks)


class Exams(StudentDetails):
    CourseCode = 108
    SeatingPlan = "26-403"

    def e1(self):
        print(self.reg, self.CourseCode, self.SeatingPlan)


class Library(StudentDetails):
    BookIssued = "Selected Works of Oscar Wilde"

    def e2(self):
        print(self.reg, self.BookIssued)


class Research(StudentDetails):
    ResearchPaper = "AI for Sustainable Development"
    ResearchValue = "10000 Dollars"

    def e3(self):
        print(self.reg, self.ResearchPaper, self.ResearchValue)


O1 = StudentDetails()
O2 = Exams()
O3 = Library()
O4 = Research()
O1.disp()
O2.e1()
O3.e2()
O4.e3()
