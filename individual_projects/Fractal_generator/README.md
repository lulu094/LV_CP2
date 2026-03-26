# Fractal Pattern Generator
LV 1st Fractal Pattern generator

## Overview

This Python program generates a Sierpinski Triangle fractal using recursion and the turtle graphics module.

The program allows the user to:
- Choose recursion depth (1–5)
- Choose triangle color
- Choose background color

## Project Structure

- main.py → Handles user interaction and runs the program
- fractal_pattern.py → Contains recursive drawing logic
- README.md → Project description

## How It Works

The program uses a recursive function called "sierpinski_triangle".

Base Case:
When depth == 0, one triangle is drawn.

Recursive Case:
The function draws three smaller triangles:
1. Bottom-left
2. Bottom-right
3. Top

Each recursive call reduces the triangle size and depth until the base case is reached.

## Concepts Used

- Recursion
- Base Case & Recursive Case
- Functional Decomposition
- Input Validation
- Turtle Graphics

## Author

lulu094