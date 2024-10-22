import random

# Generate a random number between 1, 100
number_to_guess = random.randint(1, 100)

#Initialize the attempt counter
attempts = 0

# Game loop
while True:
    # Ask the user if they would like to play
    choice = input("Are you ready to play (y/n): ").lower()
    if choice == "y":
        # Ask the user for their guess
        guess = int(input("Guess the number (between 1 and 100): "))

        # Increament the attempt counter
        attempts += 1

        # Check if guess is too low, too high or correct
        if guess < number_to_guess:
            print("Too low")
        elif guess > number_to_guess:
            print("Too high")
        else:
            print(f"Congratulations! You have guessed the number in {attempts} attempts")
    elif choice == "n":
        print("Thanks for playing. See you next time!")
        break
    else:
        print("Invalid choice")
        