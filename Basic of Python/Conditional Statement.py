# if-elif-else(SYNTAX)
# if(condition):
#     Statement1
# elif(condition):
#     Statement2
# else:
#     StatementN

# Python is INDENTATION Type language means element are correctly spaced or not/ they are space dependent.

# Traffic Lights Code
light = input("light : ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else: 
    print("light is broken")


# Grades of students
marks = input("marks : ")
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")



# Print output for :
# A = 5 & G = M
# A = 2 & G = F

A = int(input("A : "))
G = input("M/F :")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4  or  G == "F"):
    print("fee is 200")
elif(A == 5  and G == "M"):
    print("fee is 300")
else:
    print("no fee")



# Conditional statements

# Single line if/ Ternary Operator
<var> = <val1> if <condition> else <val2> 