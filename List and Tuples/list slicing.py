# list-name [starting-idx: ending-idx] endin idx is not included

marks = [85, 94, 76, 63, 48]
print(marks[1:4]) #output= [94, 76, 63]
print(marks[:4]) #output= [85, 94, 76, 63]
print(marks[1:]) #output= [ 94, 76, 63, 48]

# for negative index
print(marks[-3:-1]) #output=[76, 63]