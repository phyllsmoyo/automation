# This is guess the number game

# python module for generating random integers
import random

# storing a random number generated between 1 and 20
print("I am thinking of a number between 1 and 20")
secret_number = random.randint(1, 20)
# Count the number of guesses
guesses_taken = 0

# Ask the player to guess the number 6 times
for guesses in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    # For every increment by 1
    guesses_taken += 1

    # Message to print when number is low
    if guess < secret_number:
        print("Your guess is too low")
    # Message to print when number is high
    elif guess > secret_number:
        print("Your guess is too high")
    #  When guess == secret number : terminate the current loop and resumes execution at the next statement
    else:
        break

# Message when the number is found and number of guesses
if guess == secret_number:
    print("Good job!")
    print(f"You guessed my number in {guesses_taken} guesses")

# Message when the number is not found after 6 tries
else:
    print(f"Sorry. The number I was thinking of was {secret_number}.")
