class student:
    def getStudent(self):
        # Accept student details
        self.name = input("Name:")
        self.age = input("Age:")
        self.gender = input("Gender:")


class Test(student):

    def getMarks(self):
        # Accept class and marks
        self.studentclass = input("class:")
        print("enter the marks of respective subjects")
        self.literature = int(input("literature:"))
        self.math = int(input("Math:"))
        self.biology = int(input("biology:"))
        self.physics = int(input("physics:"))

class Marks(Test):
    # display student's information along with total marks
    def display(self):
        print("\n\nName:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Class:",self.studentclass)
        print("literature:",self.literature)
        print("math:",self.math)
        print("biology:",self.biology)
        print("physics:",self.physics)
        total_marks = self.literature + self.math + self.biology + self.physics
        if total_marks > 100:
            print("passed")
        else:
            print("failed")
            print("total marks:",total_marks)

# create an object  of Marks class
m = Marks()
# # collect student details
m.getStudent()
#
# # collect maks details
m.getMarks()
#
# # Display all information
m.display()
