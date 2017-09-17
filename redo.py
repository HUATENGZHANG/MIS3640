import turtle

ht = turtle.Turtle()

def polygon(t,n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

##polyline is composed of polygon and arch, so we can reqrite circle easily