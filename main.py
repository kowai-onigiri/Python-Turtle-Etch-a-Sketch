import turtle as t
import random

t.colormode(255)

# ----- Pencil and Canvas Creation -----
pencil = t.Turtle()
pencil.color("DarkSlateGrey")
pencil.shape("arrow")
pencil.left(90)
pencil.width(2)

screen = t.Screen()

def forward():
    pencil.forward(10)


def right():
    pencil.right(10)
    # pencil.forward(10)


def left():
    pencil.left(10)
    # pencil.forward(10)


def backwards():
    pencil.forward(-10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a_color = (r, g, b)
    return a_color


def change_color():
    color = random_color()
    pencil.color(color)


def clear_screen():
    pencil.clear()
    pencil.penup()
    pencil.home()
    pencil.left(90)
    pencil.pendown()


screen.listen()
screen.onkeypress(key="Up", fun=forward)
screen.onkeypress(key="Down", fun=backwards)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.onkey(key="space", fun=change_color)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
