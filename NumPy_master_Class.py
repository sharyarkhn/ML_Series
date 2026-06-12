from numpy import *
import numpy as np

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Python NumPy
# Numpy is a general-purpose array-processing package.
# It provides a high-performance multidimensional array 
# object and tools for working with these arrays.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Arrays in Numpy
# A NumPy array is a structured collection of elements of 
# the same data type stored in a table format.
#  ~In NumPy, arrays are called ndarray and elements are
#  accessed using square brackets [], often created from nested 
# Python lists.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Before using these functions, import NumPy:
from numpy import *

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 1. array()
# The array() function is used to create a NumPy array from a Python list or tuple.
#
# Syntax:
# array(object) #for implicit
# array(object, dtype) #for Explicit add dtype
# object → List or tuple containing elements.
# dtype (optional) → Specifies the data type of array elements.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Example
from numpy import *
arr = array([10, 20, 30, 40, 50])
print(arr) #[10 20 30 40 50]
print(arr.dtype) #int64

# Explicitly Defining Data Type
arr = array([10, 20, 30, 40, 50], float)
print(arr) #[10. 20. 30. 40. 50.]
print(arr.dtype) #float64
print(type(arr)) #

# Important Note:
# If the data type is not specified, NumPy automatically determines it based on the values provided.
# Type promotion follows:
# int → float → complex 

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Operations on NumPy Arrays
# Basically in numpy array we can't use for loop for many things like 
# if i have to add a number with each element or check any condition on 
# it or after condition we have to retrieve that value.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Convert 1 list to 1D array
list = [1,2,3,4,5]
arr1D = array(list)
print(arr1D) #[1 2 3 4 5]
print(type(arr1D)) #<class 'numpy.ndarray'>
print(arr1D.shape) # it tell Us the (row , column)

# Convert Multiple list to 2D array
list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
list3 = [3,4,5,6,7]

arrMul = array([list1 , list2 , list3])
print(arrMul)   # [[1 2 3 4 5]
                #  [2 3 4 5 6]
                #  [3 4 5 6 7]]
print(type(arrMul)) #<class 'numpy.ndarray'>
print(arrMul.shape) #(3, 5)

# WE can perform indexing on it it start from 0-(len-1)
arrEg = array([1,2,3,4,5])
print(arrEg[2]) #3

# We can change elemment as well
arrEg = array([1,2,3,4,5])
arrEg[2] = 12
print(arrEg) #[1,2,12,4,5]

# Slicing in Python means cutting out a specific piece of
# a list or an array and leaving the rest behind.
# Note: The index number where your slice ends
#       (excluded—Python stops right before this position).
# Note: If we exceed the limit it not gonna give error just print up to last index
listEg = [1,2,3,4,5,6,7,8] 
print(listEg[0:11])
print(len(listEg))
print(listEg[0] , listEg[-1])
print(listEg[:4])
print(listEg[4:]) 
print(listEg[::]) #it give us whole index
print(listEg[::-1]) #it reverse the the array [8, 7, 6, 5, 4, 3, 2, 1]
print(listEg[::-2]) #it will print in reverse reverse like first number will 
# be 8 then -2->6 then -2->4  -2->2 [8, 6, 4, 2]

# Adding a Value to Every Element
from numpy import *
arr = array([1, 2, 3, 4, 5])
print(arr) #[1 2 3 4 5]
arr = arr + 5
print(arr) #[ 6  7  8  9 10]

# Adding Two Arrays (Vectorized Operation)
# Two arrays of the same length can be added directly.
from numpy import *
arr1 = array([1, 3, 5, 7, 9])
arr2 = array([0, 2, 4, 6, 8])
arr = arr1 + arr2
print(arr) #[1 5 9 13 17]

# Checking for any Condition and retriving that
print(arr>2) #[False False  True  True  True]
print(arr[arr>2]) #[3 4 5]

# Concatenating Arrays
from numpy import *
arr1 = array([1, 3, 5, 7, 9])
arr2 = array([0, 2, 4, 6, 8])
arrCon = concatenate([arr1, arr2])
print(arrCon) #[1 3 5 7 9 0 2 4 6 8]

# Mathematical Functions on Arrays
from numpy import *
arr = array([0, 30, 60, 90])
print(sin(arr))
print(cos(arr))
print(tan(arr))
print(max(arr))
print(min(arr))
print(sqrt(arr))
print(sum(arr))
print(sort(arr))
print(mean(arr))
print(argsort(arr))
print(where(arr))

# Functions Used
# Function  Purpose
# mean()
# sin()     Calculates sine values
# cos()     Calculates cosine values
# tan()     Calculates tangent values
# max()     Returns maximum element
# min()     Returns minimum element
# sqrt()    Returns square root
# sum()     Returns sum of elements
# sort()    Sorts the array
# argsort() Returns the indices of the sorted elements.
# where()   Returns the indices of elements that satisfy a condition.

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Builtins Function In NumPy
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# linspace()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# The linspace() function creates evenly spaced numbers between a start and end value.
# Unlike range(), the ending value is included.
# If the number of parts is not specified, NumPy creates 50 values by default.
#
# Syntax:
# linspace(start, stop, num)
# start → Starting value
# stop → Ending value
# num → Number of values to generate

# Example:
from numpy import *
arr = linspace(0, 20, 5)
print(arr) #[ 0.  5. 10. 15. 20.

# Default 50 Values
arr = linspace(0, 100)
print(arr)



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#         logspace()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# The logspace() function creates numbers that are evenly spaced on a logarithmic scale.
# The generated values are powers of 10.
#
# Syntax:
# logspace(start, stop, num)

# Example
from numpy import *
arr = logspace(1, 3, 5)
print(arr) #[  10.  31.6227766   100.      316.22776602    1000. ]

# Printing with 2 Decimal Places
print('%.2f' % arr[0]) #10.00



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#         reshape()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# It is used to give shape to existing array but the twist is number 
# of element must be equal right
# Syntax:
# reshape(row , column)

# Example:
arrMul = array([[1,2,3,4,5],
          [2,3,4,5,6],
          [3,4,5,6,7]])

# we can reshape it like this is (3,5) = 15 so i can change it into (5,3) , (3,5)
arrMul = arrMul.reshape(5,3)
print(arrMul)
# [[1 2 3]
#  [4 5 2]
#  [3 4 5]
#  [6 3 4]
#  [5 6 7]]


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#          arange()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# The arange() function works similarly to Python's range() function.
# It generates values within a specified range using a step size.
#
# Syntax:
# arange(start, stop, step)

# Example
from numpy import *
arr = arange(1, 10, 2)
print(arr) #[1 3 5 7 9]




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#        logspace() [Duplicate Layout Section]
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# The logspace() function creates numbers that are evenly spaced on a logarithmic scale.
# The generated values are powers of 10.
#
# Syntax:
# logspace(start, stop, num)

# Example
from numpy import *
arr = logspace(1, 3, 5)
print(arr) #[  10.  31.6227766   100.      316.22776602    1000. ]

# Printing with 2 Decimal Places
print('%.2f' % arr[0]) #10.00


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#           zeros()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# The zeros() function creates an array filled with zeros.
#
# Syntax
# zeros(size)

# Example
from numpy import *
arr = zeros(5)
print(arr) #[0. 0. 0. 0. 0.]


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#            ones()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# The ones() function creates an array filled with ones.
#
# Syntax
# ones(size)

# Example
from numpy import *
arr = ones(5)
print(arr) #[1. 1. 1. 1. 1.]














# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#                               NumPy Random Functions
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#     random.rand()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Generates random decimal numbers uniformly distributed 
# between 0 and 1.
# Syntax
# np.random.rand(rows, columns)

import numpy as np
arr = np.random.rand(2, 3)
print(arr)
# Output
# [[0.42 0.81 0.19]
#  [0.73 0.55 0.92]]
# Notes
# Values range from 0.0 to 1.0
# Generates decimal numbers
# Shape is passed as separate arguments



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#      random.randint()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Generates random integers within a specified range.
# Syntax
# random.randint(low, high, size)
# Parameters
# low → Starting value (inclusive)
# high → Ending value (exclusive)
# size → Shape of the output array

import numpy as np
x = np.random.randint(2, 10)
print(x)
# Output
# 6
# Matrix Example
# arr = np.random.randint(1, 100, (2, 3))
# print(arr)
# Output
# [[45 12 88]
#  [71 39 54]]
# Notes
# Produces only whole numbers
# high value is excluded




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#      random.randn()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Generates random numbers from a Standard Normal Distribution.
# Syntax
# random.randn(rows, columns)

import numpy as np
arr = np.random.randn(3, 4)
print(arr)
# Output
# [[-0.52  1.20 -0.12  0.55]
#  [-1.09 -0.44  2.10 -0.88]
#  [ 0.34  0.77 -1.55  0.11]]
# Notes
# Mean = 0
# Standard Deviation = 1
# Can generate positive and negative values
# Follows a bell-curve distribution


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
#   random.random_sample()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Generates random decimal values between 0.0 and 1.0.
# Syntax
# random.random_sample(shape)

import numpy as np
arr = np.random.random_sample((2, 3))
print(arr)
# Output
# [[0.12 0.88 0.45]
#  [0.67 0.01 0.99]]
# Notes
# Values are always between 0 and 1
# Never generates negative numbers
# Shape must be provided inside double parentheses