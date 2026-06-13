# means any data.
# There are two types of attribute.
# 1) Class attribute: common for all objects. ex - college_name = "ABC College"
# 2) Instance attribute : different foe each object. Ex - self.name, self.marks

class Student :
    college_name = "ABC College"
    name = "anonymous" # class attribute

    def __init__(self, name, marks):
        self.name = name #object attribute > class attribute
        self.marks = marks
        print("adding new student in Database..")

s1 = Student ("ankur", 97)
print(s1.name)
