from turtle import Turtle, Screen

# Setup the screen
screen = Screen()
screen.title("Turtle Movement Controller")

# Create a turtle
tom = Turtle()

# Functions for movement
def move_forward():
    tom.forward(20)

def move_backward():
    tom.backward(20)

def turn_left():
    tom.left(20)

def turn_right():
    tom.right(20)

def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

# Listen for keypresses
screen.listen()
screen.onkey(move_forward, "Up")      # Move forward
screen.onkey(move_backward, "Down")   # Move backward
screen.onkey(turn_left, "Left")       # Turn left
screen.onkey(turn_right, "Right")     # Turn right
screen.onkey(clear_screen, "c")       # Clear screen and reset

# Keep the window open
screen.mainloop()
