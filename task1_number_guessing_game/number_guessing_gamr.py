# number guessing game program

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    max_attempts = 7

    print("🎯 Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}/{max_attempts}: Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number_to_guess:
            print("🎉 Correct! You guessed the number!")
            break
        elif guess < number_to_guess:
            print("Too low.")
        else:
            print("Too high.")
    else:
        print(f"❌ Game Over! The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
