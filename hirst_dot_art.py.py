import turtle as t
import random

tim = t.Turtle()
tim.width(20)
tim.speed('slow')
t.colormode(255)
tim.hideturtle()


def dot():
    tim.pd()
    tim.fd(1)
    tim.pu()
    tim.fd(50)


color_list = [(222, 152, 103), (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157),
              (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60), (116, 85, 102),
              (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119),
              (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]


x = -250
y = -200
length = 10
for i in range(length):
    tim.up()
    tim.goto(x, y)
    for n in range(length):
        color = random.choice(color_list)
        tim.color(color)
        dot()
    y += 50

my_screen = t.Screen()
my_screen.exitonclick()
