import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Timer App")
screen.bgcolor("white")  # Set background color to white
screen.setup(width=300, height=200)  # Set canvas size to 300x200

# Make the window always on top
screen.getcanvas().winfo_toplevel().attributes('-topmost', True)

# Create a turtle for drawing the timer
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, -50)  # Position the turtle at the center horizontally and y = -50
timer_turtle.color("black")

# Global variable to store the timer duration in seconds
timer_duration = 0

def set_timer_up():
    global timer_duration
    timer_duration += 60  # Increase timer by 1 minute (60 seconds)
    update_timer_display()

def set_timer_down():
    global timer_duration
    if timer_duration >= 60:
        timer_duration -= 60  # Decrease timer by 1 minute (60 seconds)
    update_timer_display()

def update_timer_display():
    timer_turtle.clear()  # Clear the previous display
    minutes = timer_duration // 60
    seconds = timer_duration % 60
    timer_turtle.goto(0, -50)  # Ensure the turtle is at y = -50
    timer_turtle.write(f"{minutes}m {seconds}s", align="center", font=("Times New Roman", 70, "bold"))  # Set font size to 70

def start_timer():
    global timer_duration
    while timer_duration > 0:
        update_timer_display()  # Update the display with the current time
        time.sleep(1)  # Wait for 1 second
        timer_duration -= 1  # Decrease the timer by 1 second
    timer_turtle.clear()
    timer_turtle.goto(0, -50)  # Position for the "Time's up!" message
    timer_turtle.write("Time's up!", align="center", font=("Times New Roman", 70, "bold"))  # Set font size to 70

# Bind the arrow keys to set the timer
screen.listen()
screen.onkey(set_timer_up, "Up")  # Increase timer with the up arrow
screen.onkey(set_timer_down, "Down")  # Decrease timer with the down arrow
screen.onkey(start_timer, "Return")  # Start the timer with the Enter key

# Keep the window open until it is closed by the user
turtle.mainloop()  # Use mainloop to keep the window open
