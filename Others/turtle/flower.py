import turtle


def draw_square(angle, rim, end):
    window = turtle.Screen()
    window.bgcolor('blue')
    james = turtle.Turtle()
    james.shape('turtle')
    james.color('white')
    james.speed(20)
    n = 0
    james.right(angle)
    while n < 4:
        james.forward(rim)
        james.right(90)
        n += 1

    if end:
        window.exitonclick()


def draw_flower():
    r = 1
    while r < 36:
        draw_square(r * 10, 200, False)
        r += 1
    draw_square(360, 200, True)


draw_flower()
