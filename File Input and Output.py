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
# 'r+' - both read and write in the file.
# 'w+' - both write and read in the file.
# 'a+' - both append and read in the file.


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