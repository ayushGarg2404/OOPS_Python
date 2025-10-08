class Student:
    def __init__(self,name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print(self.name,self.roll_no,self.marks)
    def grade(self):
        if(self.marks>=40):
            print("Pass")
            return
        else :
            print("Fail")
            return
st1 = Student("Ayush",1,50)
st2 = Student("Aditya",2,39)
st3 = Student("Mohan",3,40)
for _ in (st1,st2,st3):
    _.display()
    _.grade()


        