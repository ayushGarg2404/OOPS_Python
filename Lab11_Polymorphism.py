#design a pyhton programmer for a university system to manager student grades and evaluation,demonstrating polymorphism1.method overrriding-create a base calss person
#with method get-Role, creayte derived class student and staff taht overrride get_role
#methodoverloading - create a class grade with method calculate using default argument to handel single or multiple marks 
#Opertaor overloading create a calss score with attr marks overload the plus operator using add to sum two score objects
#create objects and demonstrate all type of polymorphism
class Person:
    def __init__(self, role):
        self.role = role
    def get_role(self):
        print(self.role)

class Student(Person):
    def __init__(self, role):
        super().__init__(role)
    def get_role(self):
        print("Student")

class Staff(Person):
    def __init__(self, role):
        super().__init__(role)
    def get_role(self):
        print("Staff")

class Grade:
    def calculate(self, *marks):
        if len(marks) == 0:
            print(0)
        elif len(marks) == 1:
            print(marks[0])
        else:
            print(sum(marks))

class Score:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
        return Score(self.marks + other.marks)
    def display(self):
        print(self.marks)

p = Person("General")
s = Student("Student")
st = Staff("Staff")
p.get_role()
s.get_role()
st.get_role()

g = Grade()
g.calculate()
g.calculate(85)
g.calculate(80, 90, 70)

s1 = Score(50)
s2 = Score(70)
s3 = s1 + s2
s3.display()
