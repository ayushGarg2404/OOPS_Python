#  a school maintains student grae in 3 subjects. write a function that returns the average marks.
#show how default parameters could be used if a student has missed a test, assume missing mark = 0
def average(sub1=0,sub2=0,sub3=0):
    return (sub1+sub2+sub3)/3
print(average(20,50))