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

# Search for a number x in this tupke using loop:

nums = [1,4,9,16,25,36,49,64,81,100]

x = 36

i = 0
while i < len(nums):
    if(nums[i] ==x):
        print("FOUND at idx", i)
    i +=1