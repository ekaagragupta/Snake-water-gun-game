import random

print("Welcome to Snake, Water, Gun Game!")

# List of valid choices
choices = ["snake", "water", "gun"]

# Computer randomly selects
computer_choice = random.choice(choices)

# User input
youstr = input("Enter your choice (snake, water, gun): ").strip().lower()

# Validate input
if youstr not in choices:
    print("Invalid input! Please enter 'snake', 'water', or 'gun'.")
else:
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {youstr}")

    # Game logic
    if youstr == computer_choice:
        print("It's a tie!")
    elif (youstr == "snake" and computer_choice == "water") or \
         (youstr == "water" and computer_choice == "gun") or \
         (youstr == "gun" and computer_choice == "snake"):
        print("You win!")
    else:
        print("You lose!")
