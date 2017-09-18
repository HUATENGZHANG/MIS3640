#Session 2 Variables, Expressions, Statements (H.T.'s review)
####### Input and Output, use print() and imput() to exceute.

####### 1.Output
# print('Hello, World!')
print('Hey,Jude','dont\'t make it bad')  # \ is escape key, 
#used to avoid python's confusion when confronting multiple quotation marks

print('The total number of overall medals in Rio 2016 is',46+38+38) #The total number of overall medals in Rio 2016 is 122
print('46+37+38=',46+37+38) # 46+37+38= 121

#######2.Input
# All input from users is read in as a STRING!!!!!!!!!!!!!!!!!!!!
# sth, when the user presses Return or Enter, the program resumes and input returns what the user typed as a string)
name = 'huateng'
print(name) #--> huateng

name = 'HT'
print('Hello,',name) #--> Hello, HT#### the second comma represents space in the result; pay attention, you don't need to put quotation around name here as it is already defined

#Extra exercise
input('Enter a number:') #--> Enter a number:, here using input function, we transfer this statement into an output. 
# Appear Enter a number: # then we enter 56
#'56' appear, which is a STRING, not a integer.
number = input('Enter a number:') #Appears Enter a number:, where we enter a random number 67
# Illustration : number = input('Enter a number:')
#Enter a number:67
print(number) # --> 67 the number we input previously appears
type(number) #--> class 'str'>, which says 67 is a string, and in order to change it into an integer
int('4') # 4, now it turns into integer. 

# So, do it again. This time we want an integer
number = int(input('Enter the number:')) # Appears Enter the number: Then I randomly put a number 50 under the TERMINAL
print(number) # Appear 50 which is an integer. To check, we run type() again
type(number) #Appear class 'str'> YEAH!!!!

######## 3. Assignment Statements
# An assignment statement creates a new VARIABLE and gives it a VALUE;
# Variables are nothing but used to store Value
message='I did something cool today!'
print(message) # I did something cool today!
pi = 3.14 # where on the right side is the value, left is the assignment. We assign the value to the assignment 
print(pi) # 3.14

first_name='Huateng'
last_name='Zhang'
print(first_name + last_name) #HuatengZhang
print(first_name, last_name) #Huateng Zhang
# Ask Python to ask user to enter the name
input('What is your first_name:')

### 3.2 Naming Convention for Variables 
# 1. anything meaningful 
# 2. any length 3. can contain letter, numbres and _
#3. not begin with numbers 4. allow upper case, prefer lower case

print('Naah, na na nanana naah, nanana naah, hey Jude.'*10)
# *10 is to repeat 10 times

###### 4.0 Expression and Statements 
#Expression is assignment statement's right side, which has value 
   # a combination of values, variables, and operators
# or a value/variable it self can be an expression.  
   # example: 1+1, 2*2, minutes/ 60, len('luther')

#Statements is a complete line of code that performs some actions, 
# to execute value, but do not have value. 
   #example: n=100, print(n)

# 4.1 Dynamic Language
a=123
print(a)
type(a) # class 'int'
a="ABC"
print(a)
type(a) # class 'str'

#4.2 = is not = in math
x=10
x=x+2
print(x) #12

#4.3 RAM Random Access Memory
a='ABC'
b=a
a='XYZ'
print(b) # ABC because b equals to the previous a, 
#when new a appears, there is no relationship between them

###### 5. Order of Operations
# For mathematical operators, python follows mathematical convention 

######6. String operations
# ''*10, means repeat the string for 10 times.
#''+'', + links them back to back 
# len(sentence) -->8, shoe the length of a chatacter 

#6.1 String Formatting 
# Formatting examples: 
#6.1.1 Integer
# '{0}, {1}, {2}'.format('a','b','c') # 'a, b, c'
'{} {}'.format('one','two') # one two
'{} {}'.format(1,2) # 1 2
'{} {}'.format('one','two') # two one, switching the order without changing the argument 

#6.1.2 Float
'{:.2f}'.format(3.14159267897887698) # 3.14 the default setting is 6 digits after decimal
# add 0.2 before f to keep 2 digits.

#6.1.3 Width
'{:09.2f}'.format(3.14159267897887698) # 000003.14, 09 determines the width of the string

################################ HOMEWORK EXERCISES#########################################
# exercise 1.1
v = (4/3)*pi*r**3
pi= 3.1415926535897931
r=5
print('The volume of a sphere with radius 5 is {:.2f}.'.format(v))

# exercise 1.2
cost = (24.95-24.95*0.4)*60+3+0.75*(60-1)
print('The wholesale cost for 60 copies is ${:.2f}.'.format(cost))

# exercise 1.3
start_time_hr=6+52/60
easy_pace_hr=(8+15/60) / 60
tempo_pace_hr=(7+12/60)/60
running_time_hr=2*easy_pace_hr + 3*tempo_pace_hr
breakfast_hr=start_time_hr+running_time_hr
breakfast_min=(breakfast_hr-int(breakfast_hr))*60 
breakfast_sec=(breakfast_min-int(breakfast_min))*60
## if turn seconds into min,hr, we use // or % to represent integer or remainder part 
print('The breakfast time is {:02d}:{:02d}:{:02d}.'.format(
    int(breakfast_hr), #只取小时的整数部分
    int(breakfast_min),
    int(breakfast_sec)))

#exercise 1.4 
per=(89-82)/82
print('the increased percentage is {:04.1f}%.'.format(per))
# 04 is the number of spaces (the width of the result)