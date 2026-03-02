# LV 1st Main Fractal Generator


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

# Import other pages
from fractal_pattern import setup_turtle, sierpinski_triangle, get_valid_depth
#Creo que asi si funciona pero aun tengo que ver si es que tiene algun defecto o error
import turtle

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
        # Necesito revisar como asegurarme que el user input sea olor y no solo un numero o letra
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

main()

# necesito un README file