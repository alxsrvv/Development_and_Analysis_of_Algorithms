import turtle
import math
n=int(input("n : "))
def path(n) :
    turtle.penup()
    turtle.speed(1)
    R=20
    turtle.pendown()
    k=0    
    turtle.left(90)
    while k!=n:
        turtle.circle(R)
        R*=-1
        turtle.circle(R)
        R*=-1
        R+=10
        k+=1
path(n)
    
