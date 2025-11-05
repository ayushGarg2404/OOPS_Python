try:
    list = []
    a = int(input("Enter number of integers: "))
    for _ in range(a):
        num = int(input("Enter a number: "))
        list.append(num)
    i = int(input("Enter index: "))
    print(list[i])
except IndexError:
    print("Wrong index")
except ValueError:
    print("Non-integrer entered")
except TypeError:
    print("Incompatible Data Types")
except:
    print("Try again")
else:
    print("Safely Exectued")

    