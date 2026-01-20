# Name: Conner Smith
# Date: January 19, 2026
# Project: Project 3C

print("Enter the integer for the player to guess.")
target = int(input())

count = 0

print("Enter your guess.")
while True:
    guess = int(input())
    count += 1

    if guess > target:
        print("Too high - try again:")
    elif guess < target:
        print("Too low - try again:")
    else:
        if count == 1:
            print("You guessed it in 1 try.")
        else:
            print(f"You guessed it in {count} tries.")
        break
