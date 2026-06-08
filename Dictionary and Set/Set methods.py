# set.add(el) is used to add an element
collection = set ()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection) #output = {1, 2}


# set.remove(el) is used to removes the element an


# set.clear() is used to empties the set
collection = set ()
collection.add(1)
collection.add(2)
collection.add("ankur yadav")
collection.add((1, 2, 3))

collection.clear()

print(len(collection) ) #output = 0


# set.pop() is used to removes a random value
collection = {"hello", "ankur yadav", "world", "coding", "python"}

print(collection.pop()) #output = hello


# set.union(set2) #combines both set values and returns new
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) #{2, 3}
print(set1)
print(set2)



# set.intersection(set2) #combines commom valuess and returns new
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2)) #{2, 3}


#IMPORTANT 
# sets are mutable buts elements are immutable, unhashable value are the list and dictionary