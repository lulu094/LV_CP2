# LV 1st Fractal Pattern Generator

# import turtle

# REQUIREMENTS
# Let the user customize the recursion depth and color of the fractal
# Make Turtle draw he Sierpinski Triangle wiht what the user has chosen
# Recursion depth should be between 1 and 5
# Use Base Case in recursion to stop it from being infinite
# If I can figure it out make a Joch Snowflake

# dictiionary of colors
# Red - #FF0000
# Green - #00FF00
# Purple - #800080
# Blue - #0000FF
# Yellow - #FFFF00

# Main Menu
# Welcome user
# ask for how they want their depth to be range 1-5
# Ask for the color they want but check it with the colors turtle accepts
# Ask user if they want to change the background color
# print "Fractal Generated Successfully" after the fractal is generated
# Have to Print it in MAIN or THE FUNCTION WHERE THEY ARE DRAWING THE TRIANGLES 
# drawing the Sierpinski Triangle
# Check if the color the user has chosen is not the sam eone as the background color
# Once drawn ask user if they want to leave 
# let them choose 3 different colors or so so that the process of drawing it can actually see it
# If == yes:
# print "Gooodbye, Thank You for using the Fractal Generator"
# if == no:
# Get them back to main
# Else:
# "Invalid input, please try again"

# do the depth the user has chosen
# User color has chosen
# make turtle draw the Sierpinski Triangle, but as it adds depth make turtle go to the mid point of the triangle to mke the next triangle
# Make turtle  draw it 
# Make sure when it turns, the turn is percise so it can actually draw a triangle
# Set the length, don't let the user choose the length of the big main triangle
# Once we have how much we want turtle to go forward and turn we need to make it run  4 times so it makes a triangle

# def sierpinski_triangle(t, depth):
#     if depth == 0:            
#         for _ in range(3):
#             t.forward(100)
#             t.left(120)
#     else:
#         sierpinski_triangle(t, depth - 1)
#         t.forward(100)
#         sierpinski_triangle(t, depth - 1) 
#         t.forward(100)
#         sierpinski_triangle(t, depth - 1)

# Inside the Sierpinski Triangle
# Recursion depth input
# Recursion will make turtle draw the triangle from the most tiny ones to the biggest one
# Makes sure the loop is not infinite by using the base case of depth == 0 - base case

# Make turtle or the terminal write "Fractal Generated succesfully" add it to this function

