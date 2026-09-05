# create an empty dictionary. Allow 4 friends to enter their favourite language as value and use keys as their names. Assume that the names are unique.

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name: lang})
name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name: lang})

print(d)

# If the value are same than second value are give a preference.
