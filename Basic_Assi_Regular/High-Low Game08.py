# High or Low Game
import random

# This function plays one round of the game
def play_round():
    # Generate random numbers for the player and computer
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    # Display the player's number
    print(f"Your number is {player_number}")
    
    # Ask the player if they think their number is higher or lower than the computer's number
    guess = input("Do you think your number is higher or lower than the computer's number? (say 'Higher' or 'Lower'): ").lower()
    
    # Check if the player's guess is correct
    if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
        print(f"Correct! The computer's number was {computer_number}. You got a point!")
        return 1  # Player gets a point for a correct guess
    else:
        print(f"Wrong! The computer's number was {computer_number}. No point.")
        return 0  # No point for a wrong guess

# This function controls the overall game
def play_game(rounds):
    score = 0  # Initialize the score
    for i in range(rounds):  # Loop through the number of rounds the player chose
        print(f"Round {i + 1}")
        print("\nStarting a new round....")
        
        # Call the play_round function to play one round and update the score
        score += play_round()
    
    # Display the final score after all rounds are finished
    print(f"Game over! Your total score is: {score}")

# Ask the player how many rounds they want to play
rounds_to_play = int(input("How many rounds would you like to play? "))  

# Start the game
play_game(rounds_to_play)
