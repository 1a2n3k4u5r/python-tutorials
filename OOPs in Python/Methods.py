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


# **** Static Method ****
# Methods that don't use the self parameter(work at class level)

# class student:
@staticmethod   #decorator which is used to remove the error in this code.

def college():
   print("ABC College")

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanentely modifying it.

# There are four pillars in the OOPs concept.

# 1) Abstraction - Hiding the implemention details of a class and only shoeing the essential features to the user.
class Car :
   def __init__(self):
      self.acc = False
      self.brk = False
      self.clutch = False

   def start(self):
         self.clutch = True
         self.acc = True
         print("car started..")

car1 = Car()
car1.start() #car started..

   

# 2) Encapsulation - Wrapping data and functions into a single unit(object).

# 3) Inheritance.
# 4) Polymorphism.

# Practice question
# Create Account class with 2 attributes-balance and account no.
# Create methods for debit,credit & printing the balance.

class Account:
    def __init__(self, balance):
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print("Debited:", amount)
        print("Current balance:", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Credited:", amount)
        print("Current balance:", self.balance)

acc1 = Account(5000)

acc1.debit(1000)
acc1.credit(500)
# **** del keyword **** #
# used to delete object properties or object itself.
 
# del s1.name #delete attribute 
# del s1  # delete object

class Student:
   def __init__(self, name):
      self.name = name

s1 = Student("shradha")
print(s1.name)
del(s1.name)


# **** Private(like) Attributes and Methods **** 
#conceptual implementation in python- Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
 
# class Student:
#    def __init__(self,name):
#       self.name = name

# s1 = Student("shradha")
# print(s1.name)


class Account:
   def __init__(self, acc_no, acc_pass):
    self.acc_no = acc_no
    self.acc_pass = acc_pass

   def reset_pass(self):
      print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.acc_pass)

# To make any attribute private we use a two Underscore(__).