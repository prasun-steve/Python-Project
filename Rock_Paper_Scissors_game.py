# Importing random
import random

# Command for a user for going through the game environment
print("Welcome to the game:\nEnter 'p' for Paper\nEnter 'r' for Rock\nEnter 's' for Scissor")

# Random guess by the computer
computer = random.choice([1,-1,0])

you = input("Enter your choice:")
# Code part
if(you == 'p' or you == 'r'or you == 's' ):
    
    # assinging to dictionaries 
    mydict = {"r" : 1 , "p" : -1 , "s" : 0}
    computerdict = {1 : "Rock" , -1 : "Paper" , 0 : "Scissor"}
    reversedict = {"r" : "Rock" , "p" : "Paper" , "s" : "Scissor"}

    # Output
    print("Computer chose ",computerdict[computer] , "\nYou chose ", reversedict[you])
    result = mydict[you] - computer
    
    if result == 0:
        print("It's a draw !!")
    elif result == -1 or result == 2:
        print("You Lose !!")
    else:
        print("You Win !!")

# For other wrong inputs
else:
    print("Please enter the correct input !!")