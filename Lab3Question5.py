for numbers in range(1,51):
    print(numbers," ")
    if numbers%3 ==0 and numbers%5 == 0:
        print("FizzBuzz ")
    elif numbers%3 == 0:  
        print("Fizz ")
    elif numbers%5 == 0:  
        print("Buzz ")
    print("\n")    