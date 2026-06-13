# Constructor
# All classes have a function called __init__(), which is always executed when the object is being initiated.
# This function is invovked(executed) at the time of object creation.
# Constructor always take an argument/parameter which is called self parameter.

# Example
class Student:

    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in Database..")
   

s1 = Student("ankur") # here paranthesis is used to call the constructor
print(s1.name) #output = ankur
 # Self is the first parameter in the constructor which is the argument

# NOTE = The (self) parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class,self is object reference.
# the data that is stored inside the class or inside the object  is calle attributes.

# Example
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
   
s1 = Student("ankur", 97)
print(s1.name, s1.marks) 

s2 = Student("arjun", 32)
print(s2.name, s2.marks) 

# Constructor are two type:
# 1) default constructor : which has only one parameter.
# Ex:
def __init__(self):
    pass


# 2) parameterized constructor : which has many or more than one parameter.
# Ex:
def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")