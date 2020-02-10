import turtle
n=int(input("n : "))
def path(n) :
    turtle.penup()
    turtle.speed(1)
    turtle.goto(-5, -5)
    turtle.pendown()
    a=10
    k=0
    while k!=n:
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.penup()
        turtle.forward(5)
        turtle.left(90)
        turtle.backward(5)
        turtle.pendown()
        a+=10
        k+=1
path(n)
