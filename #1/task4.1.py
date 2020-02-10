import turtle
n=int(input("n : "))
def path(n) :
    #turtle.penup()
    turtle.speed(1)
    #turtle.goto(-5, -5)
    #turtle.pendown()
    a=10
    k=0
    while k!=n:
        for i in range (4):
            turtle.left(90)
            turtle.forward(a)
            
        turtle.penup()
        turtle.home()
        turtle.goto(a//2,-a//2)
        #turtle.left(90)
        #turtle.backward(5)
        turtle.pendown()
        a+=10
        k+=1
path(n)
