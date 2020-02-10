import turtle

def maze_1(length):
    turtle.shape('circle')
    turtle.stamp()
    turtle.shape('arrow')
    height = length/4
    turtle.forward(length)
    new_height = height
    for i in range(9):
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(length + height)
        height = height + new_height
    turtle.right(90)
    turtle.forward(height)

maze_1(100)
