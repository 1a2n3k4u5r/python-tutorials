# Block of statements that perform a specific task
# syntax = def func_name(param1, param2..):
   #some work
# return Value
 # functions are used to reduce redundency
 # func_name(arg1,arg2). function call 
# input are know as parameter
# it is used to perform  repeated work in a easy way or in a suitable manner.


def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum
calc_sum(5, 10) #output = 15
calc_sum(2, 10)  #output = 12
calc_sum(12, 17) 

   # OR

 # this two line is called function definition where a and b are parameters
def cal_sum(a, b):
      return a + b
 
sum = calc_sum(17,2) # this line is called function call and where these values are called arguments these arguments value are stored in the parameter.

# example without using input, parameter return 
def print_hello():
    print("hello")

# print_hello() # hello
output = print_hello()
print(output) # None because it canot return value

# calculate average of 3 number

def cal_avg(a, b, c):
     sum = a + b + c
     avg = sum / 3
     print(avg)
     return avg

cal_avg(98, 97, 95)