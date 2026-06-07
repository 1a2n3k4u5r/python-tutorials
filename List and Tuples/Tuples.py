# tuples is a built-in data type lets us create immutable sequence of values means or string is also immutable.
# here we use a paranthesis at the place of square bracket
# we cannot use a assignment operator because the value is not change.

# empty value tuple
tup = ()
print(tup)
print(type(tup))
 #output = (), <class 'tuple'>

 # single value tuple always use a common
tup = (1,)
print(tup)
print(type(tup))
# output = (1,)  , <class 'tuple'>

tup = (1)
print(tup)
print(type(tup))
# output = 1 , <class 'int'>

# multiple value 
tup = (1, 2, 3, 4)
print(tup)
print(type(tup))
# output = 1, 2, 3, 4) , <class 'tuple'>


# Tuple slicing is same as the list slicing
tup = (1, 2, 3, 4)
print(tup[1:3]) # output = (2, 3)