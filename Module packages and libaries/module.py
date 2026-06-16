# *** Modules in Python ***

 
# A module is a single python file(.py)containing python code. It can include functions,classes, and variables that you can reuse in other programs.

# why we use module
# . To organize code into smaller,manageable chunks.
# . to reuse code acress multiple programs.

# Create a module

# Use the module:
import mymodule
mymodule.say_hello("ankur")
mymodule.say_bye("mahilimittra")

# variable 
from mymodule import person1
print(person1['age'])

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
# an alias is simply a new or shorter name that you give to a module, function, or object when importing it.

#Example:
import math as m
print(m.sqrt(25))
print(m.pi)

#NOTE: Original module name: math
# Alias: m
# Why use an alias?
# To make long names shorter and easier to type.
# To avoid name conflicts between modules.
# To improve readability when a module name is lengthy.

#Example 2
import mymodule as mm
mm.say_hello("Ankur")


# There are two types of module in python 
# 1) Built-in module.
# 2) External module.



# **** Built-in Modules ****
# A built-in module is a module that comes already included with Python. You do not need to install it separately using pip. You can simply import it and start using it or A built-in module is a collection of pre-written Python code that provides useful functions and features for common tasks.

#Python comes with built-in modules like
# math
# random
# os
# sys
# datetime

# Example :
import math
import random

print(math.sqrt(49))        # 7.0
print(random.randint(1, 100))  # Random number between 1 and 100

# **** External Module **** #

# An external module is a module that does not come with Python by default. You must install it separately before you can use it.

# example:
# numpy → Fast mathematical calculations
# pandas → Data analysis and spreadsheets
# requests → Make HTTP requests to websites and APIs
# flask → Build web applications
# Pillow → Work with images

#  **** dir() Function in Python ****

# The dir() function is a built-in Python function that is used to list all the attributes, methods, and functions available in an object or module.
# Examples :

 
import math
print(dir(math)) # output = ['acos', 'asin', 'atan', 'ceil', 'cos', 'degrees','factorial', 'floor', 'pi', 'pow', 'sqrt', ...]