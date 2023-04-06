import random

# The three possible moves of the user and the computer
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create a list with the possible moves
rps = [rock, paper, scissors]

# Ask the user for their move
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user >= 3 or user < 0:
    print("You typed an invaild number, you lose!")
else:
    # Print the user's move
    print(rps[user])

    # Generate a random move for the computer
    comp = random.randint(0,2)

    # Print the computer's move
    print(f"Computer Choose: {rps[comp]}")

    # Determine the winner of the game
    if user == comp:
        print("Game Draw!!")
    elif user == 0 and comp == 1:
        print("You Lose!!")
    elif user == 1 and comp == 2:
        print("You Lose!!")
    elif user == 2 and comp == 0:
        print("You Lose!!")
    else:
        print("You Won!!")
