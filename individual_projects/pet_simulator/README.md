# Pet Simulator
LV 1st Pet Simulator

## Overview

This Python program is a text-based virtual pet simulator where players can adopt, feed, play with, 
and manage multiple pets.

The program allows the user to:
- Create and manage multiple pets
- Feed pets with different types of food
- Play with pets to increase happiness
- Put pets to sleep to restore energy and health
- Breed pets with mixed genetic traits
- Shop for items using coins
- Save and load game progress
- Experience random events that affect pets

## Project Structure

- main.py - Main game loop and menu handling
- pet_class.py - Defines the Pet class and its methods
- actions.py - Functions for feeding, playing, sleeping, pet management, and the shop
- game_system.py → Handles time, random events, and save/load functionality
- savegame.txt - Stores saved game data
- inventory.csv - Tracks items purchased in the pet shop
- readme.py - Project description

## How It Works

1. Creating a Pet:
   Players enter a pet name and species. Each pet has stats: Hunger, Happiness, Energy, Health, Level, Coins, and Genes.

2. Interacting with Pets:
   - Feed: Choose basic, premium, treat, or home-cooked meals to increase hunger and happiness.
   - Play: Increases happiness but decreases energy and hunger.
   - Sleep: Restores energy and health.
   - Pet Management: Create, switch, or delete pets.

3. Random Events:
   Each hour may trigger events such as:
   - Pet getting sick (health decreases)
   - Finding a toy (happiness increases)
   - Earning coins

4. Time System:
   Hours advance with each action. A full day (24 hours) increases the day count.

5. Pet Shop:
   Spend coins to buy food, treats, toys, or home-cooked meals, which are added to inventory.

6. Breeding:
   Two pets can be bred to create a new pet with inherited genetic traits.

7. Save & Load:
   Save your pets’ stats to a file and load them later to continue playing.

## Concepts Used

- Object-Oriented Programming 
- Random Number Generation
- Functional Decomposition
- Input Validation
- Basic Game Loop & Menu System

## Author

lulu094