# how to draw the circle in one line..... 
import turtle

ht = turtle.Turtle()

print(ht)
for i in range(4):
    ht.fd(100)
    ht.lt(90)
 #draw a square with two methods

 
for i in range(4): #standard format to run 4 times
    print('Hello!')
    print(i) # so now we know how many elements 0 1 2 3

def square(t, length): #use t to generalize 
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(ht, 500) # t is just any term, generalize abstruct t, we just know, add length so we can change the length of the square

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
polygon(ht, 150, 8)

import math #as math.pi is math

def circle(t, r):
    import math
    circumference = 2*math.pi*r
    n=50
    length= circumference / n
    polygon(t, length, n)
circle(ht,90)


def arc(t, r, angle):
    arc_length=2*math.pi*r*angle/360
    n=int(arc_length/ 3)+1
    step_length = arc_length / n 
    step_angle = angle/n
    for i in range(n):
        t.fd(step_length)
        t.fd(step_angle)
arc(alex, 100, 180)

turtle.mainloop() #it moved and the default direction is from left to right, 100 pixle 

# if we invert the sequence of t and n, we still can run the whole thing with KEY WORDS, such as length=n, r=blabla
# docstring is used for documentation...
# also there are lots of functions that we can check to modify the functios...... 
# please check the link at the beginning of the page!!!!!
