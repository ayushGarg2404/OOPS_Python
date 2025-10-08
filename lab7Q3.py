class Employees:
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def calculate_salary(self):
        print(self.salary+(self.salary*35/100))
    def display(self):
        print(self.emp_id,self.name,self.salary)
emp1 = Employees(1,"Ayush",10000)
emp2 = Employees(2,"Rohan",20000)
for _ in (emp1,emp2):
    _.display()
    _.calculate_salary()
