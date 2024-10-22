import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize the attempt counter
attempts = 0

# Game loop
while True:
    # Ask the user for their guess
    guess = int(input("Guess the number (between 1 and 100): "))
    
    # Increment the attempt counter
    attempts += 1
    
    # Check if the guess is too low, too high, or correct
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
