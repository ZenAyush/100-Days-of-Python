import random

word_list = ["ardvark", "baboon", "camel", "apple", "hitman"]
lives = 6
stages = ["Full Body", "Right Leg", "Left Leg",
          "Left Hand", "Right Hand", "Chest & Neck"]

chosen_word = random.choice(word_list)
# print(f"The word is {chosen_word}")

display = []
word_lenght = len(chosen_word)-1
print(word_lenght)

for words in range(word_lenght):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:

    guess = input("Guess the word: ").lower()

    for position in range(word_lenght):
        latter = chosen_word[position]
        if latter == guess:
            display[position] = latter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You Won!")
