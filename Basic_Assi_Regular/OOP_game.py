import random

class HighLowGame:
    def __init__(self, user_number, name):
        self.name = name
        self.user_number = user_number

    def play(self):
        # Validate user input
        # Checks if self.user_number is NOT between 1 and 100:
        if not (1 <= self.user_number <= 100):
            print("Please enter a valid number between 1 and 100.")
            return

        print(f"Welcome {self.name} to the High Low game!")
        print(f"Your number is {self.user_number}")

        # Generate computer's number
        com_NUMBER = random.randint(1, 100)
        print(f"Computer's number is {com_NUMBER}")

        # Compare user_number with com_NUMBER
        if self.user_number > com_NUMBER:
            print(f"Your number ({self.user_number}) is higher than the computer's number.({com_NUMBER})")
        elif self.user_number < com_NUMBER:
            print(f"Your number ({self.user_number}) is lower than the computer's number.({com_NUMBER})")
        else:
            print(f"Your number ({self.user_number}) is equal to the computer's number.({com_NUMBER})")

# Ask for user input
while True:
    user_name = input("Enter your name: ")
    try:
        user_number = int(input(f"({user_name}) Enter a number between 1 and 100: "))
        
        # Check if the number is within the valid range
        if 1 <= user_number <= 100:
            break  # Exit loop if the number is valid
        else:
            print("Number out of range! Please enter a number between 1 and 100.")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

print(f"Welcome {user_name}, you entered {user_number}.")

# Start the game
game = HighLowGame(user_number=user_number, name=user_name)
game.play()
