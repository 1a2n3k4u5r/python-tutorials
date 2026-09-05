# write a program to input eight numbers from the user and display all the unique numbers(once).

s = set()
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))

print(s) # output = {2, 3, 4, 5, 6, 7, 8, 9}

# NOTE = yes we have a set with 18(int) and '18'(str) as a value in it.