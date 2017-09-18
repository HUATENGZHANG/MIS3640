# Session 3 Data Type ORGANIZED NOTES AND QUIZ REVIEW
# Conceptual Hierarchy:
# modules lead to program, module is a pre-written code that you can import to python. 
# statements lead to module
# expressions lead to statements
# expressions create and process objects


############################################ 1.0 Numbers 
type(3.14e-2) # class 'float'
type(123+222) # class 'int'
type(1.5*4) # class 'float'
type(2*100) # class 'int'
len(str(2**1000000)) # len() can only used to count string's length 

#Integer
print(3.14, int(3.14))           3.14 3
print(3.9999, int(3.9999))      3.9999 3 # This doesn't round to the closest int!
print(3.0, int(3.0))            3.0 3
print(-3.999, int(-3.999))      -3.999 -3  # Note that the result is closer to zero
print("2345", int("2345"))       2345 2345 # parse a string to produce an int
print(17, int(17))               17 17 # int even works on integers
print(int("23bottles"))           #ValueError

#Float
print(float("123.45"))           123.45
print(type(float("123.45")))     class 'float'

# 1.1 Import MATH
import math #whenever using math quotations, first you need to import math 
print(math.pi) # 3.141592653589793
print(math.sqrt(85)) 

# 1.2 Import Random 
import random
random.choice([1,2,3,4])

# 2 String
# can use '',"" represent. "2" is a string, not an integer

# 2.1 Escape Sign
# \, \n, \t, \\
print('I\'m \"ok\".') # \ used to avoid python's confusion
print('I\'m learning\nPython.') # \n used for vertical tab
print('\\\n\\') # Appear \\ in different lines
print('\\\t\\') # \t for horizontal tab
print(r'\\\t\\') # Appear \\\t\\  use r'' to avoid any escape 
a = """
text
text
text
"""
print(a) # triple quotation ('''or""") can display multiple line

####################################### 2.0 Boolean
# only true or false
print(True and True) # True
print(True and False)#False 
print(False and True)#False
print(False and False)#False 
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False 
print(not True) #False 
print(not False)#True

####################################### 3.0 if else, conditional statements
age = int(input('Please enter your age: ')) #RUN THIS 
if age > 21:
    print('Yes, you can.')
else:
    print('No, you are not allowed.'

##################################### Homework Session 
#Session 3
#1 and 2, check manual  

#Question: The time module provides a function, also named time, that returns the current 
# Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. 
# On UNIX systems, the epoch is 1 January 1970.

# Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds,
# plus the number of days since the epoch.


import time
print(time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
hours = (current//60)//60 % 24 #总共的小时数/24得到的余数就是除不尽的小时数，所以可以拿来用。
days = current// 60 //60 //24
print('Current time: %d days, %d hours, %d minutes and %d seconds from Epoch.' % (days, hours, minutes, second))