import turtle
import math
n=int(input("n : "))
def path(n) :
    turtle.penup()
    s=3
    turtle.speed(1)
    R=20
    a=R*(2*(math.sin(3.14159265359/s)))
    turtle.goto(R, 0)
    turtle.pendown()
    k=0
    
    turtle.left(90)
    while k!=n:
        l=90-((((s-2)/s)*180)/2)
        s+=1
        print(l)
        k+=1
        k1=0
        turtle.left(l)
        while k1!=(s-1):
            turtle.forward(a)
            turtle.left(2*l)
            k1+=1
        R+=20
        a=R*(2*(math.sin(3.14159265359/s)))
        print(R)
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(R, 0)
        turtle.left(90)
        turtle.pendown()
        
        
path(n)
