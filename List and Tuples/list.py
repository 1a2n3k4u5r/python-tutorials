# List in Python

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

# output= 94.4, 87.5, 95.2, 66.4, 45.1], <class 'list'>
#  94.4
#  87.5 
# 5
 
 # It can store elements of different typeas(integer, float, string, etc)

student = ["ankur", 95.4, 17, "Agra"]
print(student)

#output = ['ankur', 95.4, 17, 'Agra']

# IN python 
# string = immutable = things which are not change, in string index pa value ko access karna allow tha lakin value ko change karna allow nhi tha but it is vice-versa in the list.
# lists = mutable = things which are change

# str = "hello"
# print(str[0])
# str[0] = "y" #output = str' object does not support item assignment

student[0] = "arjun"
print(student) #output = ['arjun', 95.4, 17, 'Agra']