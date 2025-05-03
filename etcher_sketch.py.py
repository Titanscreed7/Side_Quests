from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)


def move_backwards():
    tim.bk(10)


def turn_right():
    tim.rt(10)


def turn_left():
    tim.lt(10)


def clear_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")


screen.exitonclick()
