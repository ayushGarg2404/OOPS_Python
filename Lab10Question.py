try:
    marks = int(input("Marks: "))
    total_marks = int(input("Totat marks: "))
    percentage = marks/total_marks*100
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Total marks cannot be zero")
except FileNotFoundError:
    print("File Not Found")
except: 
    print("Try again")
else:
    print(percentage)