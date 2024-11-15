# Guess My Number
import random

def guess():
    number_to_guess = random.randint(1, 100)
    while True:
        try:
            user_input = input("Guess the number: ")
            
            # Check if the user entered an empty input
            if user_input == "":
                print("No input provided. Exiting the game.")
                break
            
            # Convert the input to an integer
            user = int(user_input)
            
            if user > number_to_guess:
                print("Too high!")
            elif user < number_to_guess:
                print("Too low!")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  # Restart loop to prompt for input again

print("I am thinking of a number between 1 and 100...")
guess()
