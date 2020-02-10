import turtle
def path() :
    turtle.penup()
    turtle.speed(1)
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.left(90)
    a=20
    b=0
    k=1    
    t=0
    while t!=3:
        turtle.forward(a)
        turtle.right(135)
        b=a*(k*(2**0.5))
        print(a,b)
        turtle.forward(b)
        turtle.left(45)
        turtle.forward(a)        
        turtle.left(135)
        k+=1
        b=a*(k*(2**0.5))
        turtle.forward(b)
        turtle.right(45)
        k+=1
        t+=1
    turtle.right(90)
    t=0
    while t!=2:
        turtle.forward(a)
        turtle.right(45)
        turtle.forward(b)
        turtle.left(45)
        turtle.forward(a)
        turtle.left(135)
        turtle.forward(b)
        turtle.right(135)
        t+=1
    t=0
    k-=1
    while t!=3:
        turtle.forward(a)
        turtle.right(45)
        k-=1
        b=a*(k*(2**0.5))
        turtle.forward(b)
        turtle.left(135)
        turtle.forward(a)
        turtle.left(45)
        k-=1
        b=a*(k*(2**0.5))
        turtle.forward(b)
        turtle.right(135)
        t+=1
     
              
path()
