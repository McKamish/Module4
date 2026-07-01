#!/usr/bin/env python3

### Assignment Four - Dice Roller
### Author: Cory Jameson
###
###Instruction:
###When your program is run it should ...
###
###Program should start with a python shebang statement (e.g.  #!/usr/bin/env python3)
###Call the main program, by using the following code at the bottom of your program:
###
###if __name__ == "__main__":
###
###    main()
###
###The program should have at least four functions:
### main() -  Store the code that gets input from the user and then calls other functions 
### display_title() - Display the title of the program ("Dice Roller") 
### roll() - This code simulates rolling a single die and returns the value . Use the random.randint function to simulate a six-sided dice roll
### roll_dice() - This function rolls and store the value of two die (using the roll() function). 
###     Calculate the total and print the value of each die and the total. 
###     Do a check if the total is equal to 2, print "Snake Eyes!" 
###     Do a check if the total is equal to  12 print("Boxcars!")

import random

def display_title():
    print('Dice Roller!\n')

def roll():
    return random.randint(1,6)
    
def roll_dice():
    ### Determine dice rolls, and sum total
    dieOne = roll()
    dieTwo = roll()
    diceTotal = dieOne + dieTwo

    ###Print dice roll results with titles
    print(f"Die 1: {dieOne}")
    print(f"Die 2: {dieTwo}")
    print(f"Total: {diceTotal}\n")

    ###Print special cases for snake eyes and boxcars, when applicable
    if diceTotal == 2:
        print('Snake Eyes!\n')
    elif diceTotal == 12:
        print('BoxCars!\n')


def main():
    display_title()
    userRoll = input("Roll the dice? (y/n): ")
    while userRoll == 'y':
        roll_dice()
        userRoll = input("Roll the dice? (y/n): ")
    print('Thanks for playing!')


if __name__ == "__main__":

    main()
