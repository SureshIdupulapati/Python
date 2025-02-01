import random
from turtle import Turtle, Screen


def no_of_turtles():
    """Get a valid number of turtles for the race (between 2 and 10)."""
    while True:
        try:
            count = int(input("How many turtles do you want to race (2-10)? "))
            if 2 <= count <= 10:
                return count
            else:
                print("⚠️ Input is not within the range... Try again!")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 2 and 10.")


# Constants for Screen
WIDTH, HEIGHT = 500, 400
color_list = ["black", "red", "green", "yellow", "pink", "blue", "brown", "grey", "orange", "aquamarine"]

# Get user input for the number of turtles
turtles = no_of_turtles()
x_spacing = WIDTH // (turtles + 1)

# Setup the screen
s1 = Screen()
s1.setup(WIDTH, HEIGHT)
s1.title("Turtle Race 🏁")

# Betting Feature
bet = s1.textinput("Make Your Bet!", f"Choose a color from: {', '.join(color_list[:turtles])}")

# Create Turtles
turtle_list = []
for i in range(turtles):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[i])  # Assign colors correctly
    new_turtle.penup()

    # Evenly distribute turtles along the x-axis
    start_x = -WIDTH // 2 + (i + 1) * x_spacing
    start_y = -HEIGHT // 2 + 20
    new_turtle.goto(start_x, start_y)

    new_turtle.left(90)  # Face upward
    turtle_list.append(new_turtle)


def race():
    """Run the turtle race."""
    is_race_on = True
    while is_race_on:
        for t in turtle_list:
            distance = random.randint(1, 10)  # Random movement
            t.forward(distance)

            # Check if any turtle reached the finish line
            if t.ycor() >= HEIGHT // 2 - 20:
                winner = t.pencolor()
                print(f"\n🏆 The winner is the {winner} turtle!")
                if bet and bet.lower() == winner.lower():
                    print("🎉 Congratulations! Your bet was correct!")
                else:
                    print("😞 Better luck next time!")

                is_race_on = False
                break


# Start the race
race()

# Exit on click
s1.exitonclick()
