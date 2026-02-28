# LV 1st Fractal Pattern Generator

# import turtle

import turtle

# 1. Use Python's turtle module to draw a fractal.
# 2. Generate a Sierpinski Triangle using recursion.
# 3. Allow the user to:
#       - Choose recursion depth (between 1 and 5)
#       - Choose triangle color
#       - Choose background color (optional / extra credit)
# 4. Implement a proper base case to prevent infinite recursion.
# 5. Print "Fractal Generated Successfully" after drawing is complete.
# 6. Ask the user if they would like to exit or return to the main menu.
# 7. (Optional Extra Credit)
#       - Save the fractal as an image file.
#       - Implement a second fractal (Koch Snowflake).

# MAIN FUNCTION:
#   Display welcome message.
#   Ask user for recursion depth (must be between 1 and 5).
#   Validate depth input.
#   Ask user for triangle color.
#   Ask user for background color.
#   Make sure triangle color is different from background color.
#   Set up turtle screen and background.
#   Move turtle to starting position.
#   Call recursive Sierpinski function.
#   Print "Fractal Generated Successfully".
#   Ask user if they want to exit.
#       If yes:
#           Print goodbye message and close program.
#       If no:
#           Restart program.
#       Else:
#           Print invalid input message.

def main():

    while True:

        print("\nWelcome to the Sierpinski Triangle Generator!")

        # Get user inputs
        depth = get_valid_depth()
        triangle_color = input("Enter triangle color: ")
        bg_color = input("Enter background color: ")

        # Check if triangle color equals background color
        if triangle_color.lower() == bg_color.lower():
            print("Triangle color cannot be the same as background color.")
            continue

        # Setup turtle
        screen, t = setup_turtle(bg_color)

        # Draw fractal
        sierpinski_triangle(t, 400, depth, triangle_color)

        print("Fractal Generated Successfully!")

        # Ask user if they want to exit
        choice = input("Would you like to exit? (yes/no): ").lower()

        if choice == "yes":
            print("Goodbye, Thank You for using the Fractal Generator!")
            turtle.bye()
            break

        elif choice == "no":
            turtle.bye()  # close current window and restart
            continue

        else:
            print("Invalid input, restarting program.")
            turtle.bye()
            continue

# FUNCTION sierpinski_triangle(turtle, length, depth, color):

#   IF depth == 0:            ← BASE CASE
#       Draw one filled triangle.
#       Return.

#   ELSE:                     ← RECURSIVE CASE
#       1. Draw bottom-left smaller triangle
#          Call sierpinski_triangle with:
#               length / 2
#               depth - 1
#
#       2. Move turtle to bottom-right position.
#          Call sierpinski_triangle with:
#               length / 2
#               depth - 1
#
#       3. Move turtle to top-middle position.
#          Call sierpinski_triangle with:
#               length / 2
#               depth - 1
#
#       4. Return turtle to original position.
def setup_turtle(bg_color):

    screen = turtle.Screen()
    screen.bgcolor(bg_color)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(-200, -150)
    t.pendown()

    return screen, t

def sierpinski_triangle(t, length, depth, color):

    if depth == 0:  # BASE CASE
        draw_triangle(t, length, color)

    else:  # RECURSIVE CASE

        # Bottom-left triangle
        sierpinski_triangle(t, length / 2, depth - 1, color)

        # Bottom-right triangle
        t.forward(length / 2)
        sierpinski_triangle(t, length / 2, depth - 1, color)
        t.backward(length / 2)

        # Top triangle
        t.left(60)
        t.forward(length / 2)
        t.right(60)

        sierpinski_triangle(t, length / 2, depth - 1, color)

        # Return turtle to original position
        t.left(60)
        t.backward(length / 2)
        t.right(60)

def get_valid_depth():

    while True:
        try:
            depth = int(input("Enter recursion depth (1-5): "))

            if 1 <= depth <= 5:
                return depth
            else:
                print("Depth must be between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# FUNCTION draw_triangle(turtle, length, color):
#   Begin fill with chosen color.
#   Repeat 3 times:
#       Move forward length.
#       Turn left 120 degrees.
#   End fill.

def draw_triangle(t, length, color):

    t.fillcolor(color)
    t.begin_fill()

    for _ in range(3):
        t.forward(length)
        t.left(120)

    t.end_fill()

main()