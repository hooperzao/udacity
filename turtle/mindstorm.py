import turtle


def draw_shape(shape):
    window = turtle.Screen()
    window.bgcolor('blue')
    scarlet = turtle.Turtle()
    scarlet.shape('turtle')
    scarlet.color('green')
    scarlet.speed(2)

    if shape == 'rec':
        num = 0
        while num < 4:
            scarlet.forward(100)
            scarlet.right(90)
            num += 1

    if shape == 'cir':
        scarlet.circle(100)

    if shape == 'tri':
        num = 0
        while num < 3:
            scarlet.forward(100)
            scarlet.right(120)
            num += 1

    window.exitonclick()


draw_shape('tri')
