# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:
import random as rd

def high_low_game():
    total = 1  # Start with round 1
    while True:
        user_input = input("Do you want to play the High_Low game (Yes/Enter): ").strip().capitalize()
        
        if user_input.lower() == "Yes":
            print(f"\nRound {total}")  # Display the round number only after the user says "Yes"
            try:
                user_num = int(input("Enter a number between 1 and 100 and (Guess my number): "))
                
                if 1 <= user_num <= 100:
                    coma_an = rd.randint(1, 100)  # Random number between 1 and 100
                    
                    if user_num > coma_an:
                        print(f"Your number {user_num} is higher than the number I have chosen {coma_an}")
                    elif user_num < coma_an:
                        print(f"Your number {user_num} is lower than the number I have chosen {coma_an}")
                    else:
                        print(f"Your number {user_num} is equal to the number I have chosen {coma_an}")
                else:
                    print("Please enter a number between 1 and 100.")
                    
            except ValueError:
                print("Invalid input! Please enter a valid number between 1 and 100.")
        
            total += 1  # Increment the round count after each valid round

        elif user_input == "":
            print("Thanks for playing! Goodbye!")
            break  # Exit the game
        
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")
        
# Call the function to start the game
high_low_game()
