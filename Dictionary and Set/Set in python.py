# set is the collection of the unordered items.
# Each element in the set must be unique and immutable. 
# these are the value which is store in the set are Boolean, integer, float,string, tuple, etc are immutable but list and dictionary are not stored in the set.
# Duplicate values are ignored
# repeated elements stored only once, so it resolved to {1,2}

collection = {1, 2, "hello", "world"}
print(collection)
print(type(collection))  #output = {'world', 1, 2, 'hello'} ,  <class 'set'>


# empty set syntax
# collection = ()  they are class dictionary
collection = set()
print(type(collection)) #output = <class 'set'>

