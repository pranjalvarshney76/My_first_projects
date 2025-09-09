# Guess the Number Game

import random


secret_number = random.randint(1, 100)

print("Welcome to the Guess the Number Game!")
print("I have chosen a number between 1 and 100.")
print("Can you guess it?")


while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it right.")
        break
