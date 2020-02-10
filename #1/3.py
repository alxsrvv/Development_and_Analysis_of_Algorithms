import turtle

def off_white():
    save_length = 15
    length = save_length
    hight = 20
    turtle.penup()
    turtle.goto(-200,0)
    turtle.shape('circle')
    turtle.stamp()
    turtle.shape('arrow')
    turtle.left(90)
    turtle.pendown()
    turtle.forward(hight)

    def path():
        length = 20
        turtle.right(135)
        turtle.forward(hight)
        turtle.left(45)
        turtle.forward(length)
        turtle.left(135)
        length+=save_length
        turtle.forward(length)
        turtle.right(45)
        turtle.forward(hight)

    path()


off_white()
