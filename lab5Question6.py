#design a fn studentRecord(course,*subject,**details) taht stores the course name, store multiple subject using subject argument, stores details like age,grade,name using details argument.write a program that demonstrate all three cases in fn call
def studentRecord(course,*subject,**details):
    print(course,subject,details)
print(studentRecord("comp","python","rdms","oops",Name= "Ayush",Grade= "A",Age = 19))


