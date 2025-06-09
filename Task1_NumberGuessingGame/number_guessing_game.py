import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("This project is developed by Naveen Thummala.\n")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    else:
        print(f"😢 Game Over! The number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()