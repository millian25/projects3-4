import random
def guessing_game():
    while True:
        choice = input("Are you ready to start the game? (yes/no): ").lower()
        if choice == "yes":
            round1 = random.randint(1, 100)
            round2 = random.randint(1, 100)
            print(f"{round1}, {round2}")
        elif choice == "no":
            print("Thanks for playing")
            break
        else:
            print("Invalid choice")
guessing_game()

        