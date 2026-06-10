# there are two types of functions
# 1) Built-in functions are print(),already print in python
# len(), which is used to return the number of items in a container
# type(),
# range()

# 2) user defined functions, are those which are built by the programmer

# Example
print("ankuryadav") #where print is a function call where ankuryadav is a arguments

print("ankuryadav",end="$") #sep = " "
print("engineer") #end = "\n"
# output = ankuryadav$engineer

# DEFAULT PARAMETER = Assigning a default value to parameter,which is used when no argument  is passed

#example

def cal_prod(a=1,b=2):
    print(a * b)
    return a * b

cal_prod() #2

# OR
def cal_prod(a,b = 3):
    print(a * b)
    return a * b

cal_prod(1) # 3 because we consider a not assign value is 1 but the vice-versa of these example is not consider

#  def cal_prod(a=4,b ):
#     print(a * b)
#     return a * b
# cal_prod(1) # error

# Write a function to print the length of a list.(list is the parameter)

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "agra"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities) #6
print_len(heroes) #4


# Write a function to print the element of a list in a single line.(list is the parameter)

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "agra"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)
print()


# Write a function to find the factorial of n.(n is the parameter)

def  cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(5)


# Write a function to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(73) # 73 USD = 6059 INR