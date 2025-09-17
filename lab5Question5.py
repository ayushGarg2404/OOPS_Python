#write a fn bonus(salary,rate = 0.10) that calcualte the new salary after applying the bonus rate. call the fn once using positional argument and once using keyword arguments.show a case where incorrect mixing of positon and keyword arguement show error
def bonus(salary,rate = 0.10):
    return salary+(salary*rate)
print(bonus(10000,0.2),bonus(salary=5000,rate=0.5))
print(bonus(rate=10,25000))