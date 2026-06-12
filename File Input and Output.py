# Python can be used to perform operations on a file.(write and read data).
# RAM is a volatile memory,fast in execution,data is not permanentely stored.
# For permanently stored information we stored in the form of files.

# Tyoes of all files.
# 1) Text Files:.txt,.docx,.log etc. or data is stored in the form of character
# 2) Binary Files:.mp4,.mov,.png,.jpeg etc.

# Both the file is used to store finally in the form of bits.

# ***** OPEN,READ and CLOSE FILE ***** #
# We have to open a file before reading or writing.

# f = open("file_name", "mode")
# where file_name = sample.txt,demo.docx
# where mode = r: read mode, w: write mode.
# If any mode is not define than we read the file.

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data)) 
f.close()
#I am learning 
# Python from ApnaCollege.
# <class 'str'>

# There are many types of mode.
# 'r' - open for reading(default).
# 'w' - open for writing,truncating the file first.
# 'x' - create a new file and open it for writing.
# 'a' - open for writing,appending to the end of the file if it exists.
# 'b' - binary Mode 
# 't' - text mode (default)
# '+' - open a disk file for updating(reading and writing)
# 'r+' - read and write in the file, in this file is  not truncate, the stream is positioned at the begining of the file, in this mode file is overwrite at the begining.
# 'w+' - both write and read in the file ,in this mode file is truncate means file data is deleted .
# 'a+' - both append and read in the file, stream is positioned at the end of file, it is not truncate.




#  **** Reading a file ****



#data = f.read()  # reads entire file
#data = f.readline() # reads one line at a time

f= open("demo.txt", "r")

data = f.read(5)
print(data)

f.close()
# I am 

f= open("demo.txt", "r")

line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)

f.close()
# output = I am learning 

# Python from ApnaCollege.



# **** Writing to a file ****



f = open("demo.txt","w")
f.write("this is a new line") # "overwrites the entire file"

f = open("demo.txt","a")
f.write("this is a new line")


f = open("demo.txt", "a")
f.write("\n After that node.js" \
"")

f.close()

f = open("sample.txt", "a")
f.close() # use to create a file.

# example of r+.
f = open("demo.txt", "r+")
f.write("abc")
f.close()




# with Syntax
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

# where f = alias(nickname)
# when we use a with syntax we don't need to use f.close()



# DELETING A FILE


# using the os module (where os is operating system).
# Module( like a code library)is a file written by another programmer that generally has a function we can use.
# for install new module = we use (pip install_)
#for version check = (pip3 install_) 

# import os
# os.remove()



# Practice question
# Create a new file "practice.txt" using python. Add the following data in it:
 # Hi everyone
 # we are learning file input and output
 # using java
 # I like programming in java.


with open("practice.txt","w") as f:
   f.write("Hi everyone \n we are learning file input and output \n")
   f.write("using Java. \n I like programming in Java.")

   # Write a function that replace all occurences of "java" with "python" in above file.

with open("practice.txt","r") as f:
   data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)


# Search if the word "learning" exists in the file or not.

word = "learning"
with open("practice.txt","r") as f:
   data = f.read()
   if(data.find(word) != -1):
      print("Found")
   else:
      print("not found")

