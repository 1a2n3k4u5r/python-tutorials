# A variable is a name given to a memory location in a program.

# Example =
name = "Ankur" # where name is the variable and Ankur is a value in the string.
age = 22 # age = Integer.
Income = 25000.05 # price = float.

print(name)
print("my name is :", name) # my name is : Ankur
print("my age is :", age) # my age is : 22


name = "ankur"
age = 25
price = 25.99

age2 = age

print(age2) # 25



#  ****Rules for identifers****



# Identifiers can be combination of uppercase and lowercase letter, digits or an underscore(_). so myVariable,variable_1,variable_for_print all are valid python identifiers.
# An identifier can not start with digit.So while variable1 is valid,1variable is not valid.
# we cannot use special symbols like !,@,#,$,% etc in our identifier.
# Identifier can be of any length.


name = "Ankur Yadav"
age = 22
price = 25.99

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(price)) # <class 'float'>