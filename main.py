import random
import os
import art

game = True

while game:

    print(art.logo)

    print("Welcome to the number Guessing Game!")
    print("I am thinking of a number between 1 and 100: ")

    check = True
    while check:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level.lower() == 'easy' or level.lower() == 'hard':
            if level.lower() == 'easy':
                attempts = 10
            elif level.lower() == 'hard':
                attempts = 5
            check = False

    number = random.randint(1, 100)

    while attempts > 0:

        if attempts == 1:
            print(f"You have {attempts} attempt remaining to guess the number.")
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")

        check = True
        while check:
            guess = (input("Make a guess: "))
            if guess.isnumeric():
                guess = int(guess)
                check = False
            else:
                print("That is not a number.")

        if guess == number:
            print(f"You got it! The answer was {number}.")
        elif guess < number:
            print("Too low.")
            attempts -= 1
        elif guess > number:
            print("Too high.")
            attempts -= 1

        if attempts > 0 and guess != number:
            print("Guess again.")
        elif attempts == 0 and guess != number:
            print(f"You have run out of guesses, you lose. The answer was {number}.")

        if guess == number or attempts == 0:
            check = True
            while check:
                again = input("Do you want to play again? Type 'yes' or 'no': ")
                if again.lower() == "yes" or again.lower() == "no":
                    check = False
            if again.lower() == "yes" or again.lower() == "no":
                break

    if again.lower() == 'no':
        game = False

    os.system("clear")
