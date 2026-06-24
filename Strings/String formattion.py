# **** String Formating in Python ****
# string formatting means inserting values into strings in a clean and readable way.
# In Python, string formatting means inserting values into strings in a clean and readable way.

# F-Strings
# F-String allows you to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal, like this:
# Example : 
txt = f"The price is 49 dollars"
print(txt)


# **** Placeholders and Modifiers ****

# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

# Examples :
price = 59
txt = f"The price is {price} dollars"
print(txt)

# NOTE: 
# A placeholder can also include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

# Example :
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)



#  **** Perform Operations in F-Strings ****

txt = f"The price is {20 * 59} dollars"
print(txt) #The price is 1180 dollars

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt) # The price is 73.75 dollars


price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt) # It is very Cheap



# **** Execute Functions in F-Strings ****
# Use the string method upper()to convert a value into upper case letters:

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


# ****  More Modifiers ****
# At the beginning of this chapter we explained how to use the .2f modifier to format a number into a fixed point number with 2 decimals.

# There are several other modifiers that can be used to format values:
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)  


# **** String format() ****
# we used the format() method to format strings.

# NOTE: The format() method can still be used, but f-strings are faster and the preferred way to format strings.
# The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))  # The price is 49 dollars


# **** Multiple Values ****
# If you want to use more values, just add more values to the format() method:
itemno = 23
count = 5
txt_multi = "The price is {} dollars, item no {}, count {}"
print(txt_multi.format(price, itemno, count))  # The price is 49 dollars, item no 23, count 5

# **** INDEX NUMBERS ****
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))   # I want 3 pieces of item number 567 for 49.00 dollars.

#  **** Named Indexes ****
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):


myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang")) # I have a Ford, it is a Mustang.