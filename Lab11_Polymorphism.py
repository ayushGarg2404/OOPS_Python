#design a pyhton programmer for a university system to manager student grades and evaluation,demonstrating polymorphism1.method overrriding-create a base calss person
#with method get-Role, creayte derived class student and staff taht overrride get_role
#methodoverloading - create a class grade with method calculate using default argument to handel single or multiple marks 
#Opertaor overloading create a calss score with attr marks overload the plus operator using add to sum two score objects
#create objects and demonstrate all type of polymorphism
class Person:
    def __init__(self,role):
        self.role = role
    def get_role(self):
        print(self.role)

class Student(Person):
    def __init__(self,role):
        super().__init__(role)
    def get_role(self):
        print("Student")
class Staff(Person):
    def __init__(self,role):
        super().__init__(role)
    def get_role(self):
        print("Staff")
class Grade:
    def __init__(self):
        return
    def calculate(self):
        print("0")
    def calculate(self,a):
        print(a)
    def calculate(self,a,b):
        print(a+b)


        