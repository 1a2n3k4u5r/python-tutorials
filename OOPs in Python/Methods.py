# Methods are functions that belongs to objects.

# creating class
class Student:
  def __init__(self,fullname):
    self.name = fullname

  def hello(self):
    print("hello", self.name)
    
 #creating object
s1 = Student("ankur")
s1.hello()

# In class two things are stored
# 1) Data(attributes)
# 2) Method

# Example
class Student:
  college_name = "ABC College"

  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def welcome(self):
    print("welcome student", self.name)

  def get_marks(self):
    return self.marks
  
s1 = Student("ankur", 97)
s1.welcome()
print(s1.get_marks())

# Create student class that takes name and marks of 3 subjects as argument in constructor.then create a method to print the average.
  
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hi", self.name, "your avg score is:", total / len(self.marks))

s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()