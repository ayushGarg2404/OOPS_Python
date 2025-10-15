#SChool has person,techer,class teahcer, each level has its own properties and methods
class Person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name,end=" ")
class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject
    def display(self):
        super().display()
        print(self.subject,end=" ")
class ClassTeacher(Teacher):
    def __init__(self, name, subject,section):
        super().__init__(name, subject)
        self.section = section
    def display(self):
        super().display()
        print(self.section,end=" ")
pr1 = Person("Mohan")
tc1 = Teacher("Rohan","Maths")
ct1 = ClassTeacher("Sam","Science","A")
for i in(pr1,tc1,ct1):
    i.display()
    print()