try:
    bs_Sal = int(input("Base Salary: "))
    hra = int(input("hra: "))
    da = int(input("da: "))
    gross_sal = bs_Sal+hra+da
except ValueError:
    print("Enter numeric values")
except TypeError:
    print("Unsupported Data type")
except KeyboardInterrupt:
    print("Keyboard Interrupt")
except:
    print("try again")
else:
    print(gross_sal)
