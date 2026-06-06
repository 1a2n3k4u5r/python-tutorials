# list.append adds one element at the end
list = [2, 1, 3]
list.append(4)
print(list) #output = [2, 1, 3, 4]


# list.sort is used to sort/arrange in ascending order
# print(list.append(4)) #output = None
print(list.sort()) #output = None
print(list) #output = [1, 2, 3, 4]


# list.sort(reverse=True) is used to sort in descending order 
print(list.sort(reverse=True))
print(list) #output = [4, 3, 2, 1]


# list.reverse() is used to reverses list 
list.reverse()
print(list) #output = [1, 2, 3, 4]


# list.insert(idx, el) is used to insert element at index
list.insert(1,5)
print(list) 

# list.remove() is used to remove first occurence of element

# list.pop(idx) is used to remove element at idx