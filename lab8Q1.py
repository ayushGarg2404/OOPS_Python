#create a base class person with attributes name,age.create a derive class employee that inherits from person
#and adds atrbts emp_id,salary 

#implement multi level inheritance with the class manager derive from employee with a department attribute
#implement multi level inheritance with class trainer that inherits from employee and certification
#write appropriate method to display all details for each type of emplyee
#create obj for each class and display their information
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age,end=" ")
class Employee(Person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id =emp_id
        self.salary= salary
    def display(self):
        super().display()
        print(self.emp_id,self.salary,end=" ")
class Manager(Employee):
    def __init__(self, name, age, emp_id, salary,department):
        super().__init__(name, age, emp_id, salary)
        self.department = department
    def display(self):
        super().display()
        print(self.department,end=" ")
class Certification:
    def __init__(self,certificate):
        self.certificate = certificate  
    def display(self):
        print(self.certificate,end=" ")   
class Trainer(Employee,Certification):
    def __init__(self, name, age, emp_id, salary,certificate):
        Employee.__init__(self,name,age,emp_id,salary)
        Certification.__init__(self,certificate)
    def display(self):
        Employee.display(self)
        Certification.display(self)

p1 = Person("Ayush",19)
emp1= Employee("Ram",20,1,10000)
mng1 = Manager("Sam",21,2,20000,"Editing")
cer1 = Certification("BTECH CSE DEGREE")
tr1 = Trainer("Bam",22,3,15000,"BTECH CSE DEGREE")
for i in (p1,emp1,mng1,cer1,tr1):
    i.display()
    print()
   






