# Loops are used to repeat instructions
# lookps are two types
# 1) while loop
# 2) for loop


count = 1   # variables in python are iterator or loop ka andar run karna ko iteration
while count <=5 :
    print("hello")
    count +=1

print(count) #output = 5 times hello, and 6
            
#             # OR

i = 1
while i <= 5 :
    print("Ankur Yadav")
    i+=1   

#               # OR 

i = 1
while i <= 10 :
    print("ankur yadav", i) 
    i+=1    # output = ankur yadav 1, ankur yadav 2,ankur yadav 3, ankur yadav 4,ankur yadav 5,ankur yadav 6,ankur yadav 7,ankur yadav 8,ankur yadav 9,ankur yadav 10

# # print numbers from 1 to 5
i = 1
while i <= 5 :
    print(i)
    i +=1   # output : 1,2,3,4,5

#     # print("Loop ended")
   

#    # print numbers from 1 to 100

i = 1
while i <= 100 :
    print(i)
    i += 1
  
  # for reverse
i = 100
while i >= 1 :
    print(i)
    i -= 1
  
#  #print the multiplication table of a number n.
i = 1
while i <= 10 :
    print(3 *i )
    i += 1
  
# Print the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(nums): 
   print(nums[i])
   i += 1

    #traverse meaning travell karna har ek element par            

# Search for a number x in this tuple using loop:

nums = [1,4,9,16,25,36,49,64,81,100]

x = 36

i = 0
while i < len(nums):
    if(nums[i] ==x):
        print("FOUND at idx", i)
    i +=1
else:
    print("finding..")  


# Break & Continue  in Loop

# Break: used to terminate the loop when encountered.

# Continue: terminate execution in the currrent iteration & continue execution of the loop with the next iteraion.

# examples of Break
i = 1
while i <=5 :
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop") #output = 1, 2,3 end of loop


nums = [1,4,9,16,25,36,49,64,81,100]

x = 36

i = 0
while i < len(nums):
    if(nums[i] ==x):
        print("FOUND at idx", i)
        break
    else: 
        print("finding..")
    i += 1

print("end of loop")

# examples of Continue

i = 0
while i <= 5:
    if(i == 3):
        i +=1
        continue #skip
    print(i)
    i +=1 #output = 0, 1, 2, 4, 5.

# for loops in python
# loops are used for sequential traversal. For traversing list,string,tuples etc.

# list = [1, 2, 3]
#   for el in list:
#     print(el)

#example
veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]

for val in veggies:
    print(val) #output = potato,brinjal,ladyfinger,cucumber.


# for loop with else
# for el in list:
#     print(el)
# else:
#     print("END")

str = "apnacollege"

for char in str:
    print(char)
else:
    print("END")

    # OR

    str = "apnacollege"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END")


# Print the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el)

# Search for a number x in this tuple using loop:

nums = [1,4,9,16,25,36,49,64,81,100,49]
x = 49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
    idx +=1


# ****IMPORTANT****
 # RANGE
#  Range function returns a sequence of numbers,starting from 0 by default, and increments by 1(by default), and stops before a specified number
# range(start?,stop,step?)
# for el in range(5):
#     print(el)
# for el in range(1,5):
#     print(el)
# for el in range(1, 5, 2):
#     print(el)

seq = range(10)

for i in seq:
    print(i) # it canot consider the last number


# for i in range(10):  #range(stop)
#     print(i)

# for i in range(2, 10) : #range(start, stop)
#     print(i)


for i in range(1, 100, 2): #range(start, stop, step)
    print(i)

for i in range(1, 100, 2): 
 print(i) # for  print odd no

 for i in range(2, 100, 2): 
    print(i) # for  print even no 


 # print number from 1 to 100
 for i in range(1, 101): 
    print(i)


# print number from 100 to 1
 for i in range(100, 0, -1): 
    print(i)

 # Print the multiplaction table of a number n   
n = int(input("enter number : "))
 
for i in range(1,11):
     print(n * i)


# pass Statement
# pass is a null statement that does nothing. it is used as a placeholder for future code

# for el in range(10):
# pass

for i in range(5):
    pass
if i > 5:
    pass
print("some useful work")

# write a program to find the sum of first n natural number.
n = 5

sum = 0
for i in range(1, n+1):
    sum += i

print("total sum =", sum)

# Write a program to find the factorial of first n number(using for)
n = 5
fact = 1

for i in range(1, n+1):
    fact *= 1
print("factorial =", fact)