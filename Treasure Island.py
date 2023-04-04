# This line welcomes the user to the game.
print("Welcome to Treasure Island.")

# This line explains the user's mission in the game.
print("Your mission is to find the treasure.")

# This line prompts the user to make a choice between going left or right.
chuj = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")

# This block of code executes if the user chooses to go left.
if chuj == "left":
    # This line prompts the user to choose between waiting for a boat or swimming across a lake.
    chuj = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    
    # This block of code executes if the user chooses to wait for a boat.
    if chuj == "wait":
        # This line prompts the user to choose between three doors of different colors.
        chuj = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")

        # This block of code executes if the user chooses the yellow door.
        if chuj == "yellow":
            # This line congratulates the user for finding the treasure and declares the user as the winner of the game.
            print("Congrats!! You found the treasure, You Won!!")
        
        # This block of code executes if the user chooses the blue door.
        elif chuj == "blue":
            # This line informs the user that they have been beaten by a "Gain Meta Human" and died, and that the game is over.
            print("You have been beaten by Gain Meta Human and you are dead. Game Over!!")
        
        # This block of code executes if the user chooses any door other than the yellow or blue one.
        else:
            # This line informs the user that they have opened the door behind which a tiger was craving since 2 months, and that the game is over.
            print("Behind this door, a tiger was craving since 2 months. Game Over!!")

    # This block of code executes if the user chooses to swim across the lake.
    else:
        # This line informs the user that they have been eaten by piranhas and that the game is over.
        print("You have been eaten by the piranhas. Game Over!!")

# This block of code executes if the user chooses to go right.
else:
    # This line informs the user that they have been hit by a truck and that the game is over.
    print("You have been hit by a truck. Game Over!!")
