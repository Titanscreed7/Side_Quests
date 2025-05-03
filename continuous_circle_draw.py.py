import random
import turtle as t

tim = t.Turtle()

# for i in range(10):
#     for i in range(15):
#         tim.penup()
#         tim.fd(10)
#         tim.pd()
#         tim.fd(10)
#     for _ in range(3):
#         tim.color("navy")
#         tim.fd(100)
#         tim.rt(120)
#
#     for i in range(4):
#         tim.color('red')
#         tim.forward(100)
#         tim.right(90)
#
#     for _ in range(5):
#         tim.color("blue")
#         tim.fd(100)
#         tim.rt(72)
#
#     for _ in range(6):
#         tim.color("green")
#         tim.fd(100)
#         tim.rt(60)
#
#     for _ in range(7):
#         tim.color("orange")
#         tim.fd(100)
#         tim.rt(51.4285714286)
#
#     for _ in range(8):
#         tim.color("pink")
#         tim.fd(100)
#         tim.rt(45)
#
#     for _ in range(9):
#         tim.color("yellow")
#         tim.fd(100)
#         tim.rt(40)
#
#     for _ in range(10):
#         tim.color("black")
#         tim.fd(100)
#         tim.rt(36)
#
#     sides = 4
#     angle = 360 / sides

t.colormode(255)
tim.width(2)
tim.speed(0)
# colors = ["black", "yellow", "pink", "orange", "green", "blue", "red", "navy", "purple",
#           "violet", "magenta", "turquoise", "cyan"]
# distance = 15
# angle = [0, 90, 180, 270]


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


radius = 100

for _ in range(72):
    tim.color(random_colour())
    tim.circle(radius)
    tim.rt(5)
# def random_walk(walk_distance):
#     tim.color(random_colour())
#     tim.rt(random.choice(angle))
#     tim.fd(walk_distance)
#
#
# for i in range(400):
#     random_walk(distance)


screen = t.Screen()
screen.exitonclick()
# import heroes
