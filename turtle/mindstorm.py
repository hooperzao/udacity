import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor('blue')

    scarlet = turtle.Turtle()
    scarlet.shape('turtle')
    scarlet.color('green')
    scarlet.speed(2)
    scarlet.forward(100)
    scarlet.right(90)
    scarlet.forward(100)
    scarlet.right(90)
    scarlet.forward(100)
    scarlet.right(90)
    scarlet.forward(100)
    scarlet.right(90)

    window.exitonclick()


draw_square()
