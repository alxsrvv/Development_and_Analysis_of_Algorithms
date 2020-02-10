import turtle

def mirror(height):
    length = height/8
    turtle.shape('circle')
    turtle.stamp()
    turtle.shape('arrow')
    turtle.right(90)

    def rorrim(four):
        for i in range(four):
            turtle.forward(height)
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(height)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            
    rorrim(4)
    
    turtle.stamp()
    turtle.penup()
    turtle.goto(length,-height)
    turtle.left(180)
    turtle.pendown()
    
    rorrim(4)
    turtle.stamp()
        
mirror(100)
