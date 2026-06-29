# Why use NUMPY
# NumPy space bachata hai.
# NUmpy provides efficient storage.
# It also provides better ways of handling data for processing.
# It is fast.
# It is easy to learn.
# NumPy uses relatively less memory to store data.


# **** Array creation of numpy **** #
# There are five ways to create numpy array 
# 1)Conversion from other python structures.(e.g.,lists,tuples)
# 2)Intrinsic numpy array creation objects(e.g.,arange,ones,zeros,etc.)
# 3)Reading arrays from disk,either from standard or custom formats.
# 4) Creating arrays from raw bytes tgrough the use of strings or buffers.
# 5) Use of special library functions(e.g.,random)



 # **** WELCOME TO NUMPY TUTORIAL **** #
# import numpy as np
# myarr = np.array([3,6,32,7], np.int8)
# print(myarr) output are = array([3  6 32  7], dtype=int8 )  

# import numpy as np
# myarr = np.array([[3, 6, 37, 7]], np.int64)
# myarr[0,1] #Output = 6

# myarr.shape
# output = (1,4)


# myarr.dtype
# output = dtype('int64')


# **** Array creation: Conversion from other Python structures **** #

# listarray = np.array([[1,2,3],[5,8,5,],[0,3,1]])
# listarray # output = array([[1,2,3],
# [5,8,5],
# [0,3,1]])

# listarray.dtype  #output = dtype('int32')

# listarray.shape #output = (3,3)
# listarray.size  #output = 9

#np.arra({34,23,23})
# output are = array({34, 23}, dtype=object)


# zeros = np.zero((2,5))
#zeros
# output are = array([[0.,0.,0.,0.],[0.,0.,0.,0.,]])


# rng = np.arange(15)
#rng
# output are = array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])


# lspace = np.linspace(1,5,14) ya par huma 1 se 5 tak linearly space 12 element dega or jisma 1 hamara first element hota hai or 5 hamara last element hota hai.
#lspace 
# output = array([1.   , 2.3333333,  3.66666667, 5.      ])

# emp = np.empty((4,6))
# emp
# array([[random no.]])

#emp_like = np.empty_like(lspace)
#emp_like
# output = array([1.   2.333333, 3.6666666667, 5.      ])


# ide = np.identity(45)
# ide   
# output are = identity matrix of 45


# ide.shape
#(45,45)

# arr = np.arange(99)
# arr
# output are = array([0,1,2,3,4,5,6,7,8,9..................98])


# arr.reshape(3,33) yha par 3*33 element milta ha. or yha par reshape nhi hoga.

# arr = arr.reshape(3,33) yha par reshape ho jayga.
# arr


# arr.ravel() yha par array ekdum sidha hojayga or 1-D array banjayga