import random

print("Welcome to Zuhab's Guessing game\nI am thinking of a number between 1 and 100\nYou will have 10 guesses to guess my number")
n = random.randint(1, 100)

guess_count = 0

guess_limit = 9  # Count is 10

while guess_count <= guess_limit:
    try:
        guess = int(input("Enter an integer from 1 to 100: "))

        guess_count += 1

        if guess < n:
            print("Unlucky, your guess is too low!")

        elif guess > n:
            print("Unlucky, your guess is too high!")

        elif guess == n:
            print("you guessed it in ", guess_count, "Guesses")

            break
    except ValueError:
        print("Invalid Data Type")
else:

    print("Sorry, the correct number is", n)
