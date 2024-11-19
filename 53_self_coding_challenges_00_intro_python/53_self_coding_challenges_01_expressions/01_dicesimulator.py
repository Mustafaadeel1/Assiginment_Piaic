# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
import random 

def main():
    user = input("Simulate rolling two dice, three times :) To start the game, type 'Start': ").lower()
    
    if "start" == user:  
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        die3 = random.randint(1, 6)  
            
        print(f"Roll : Die 1 rolled a {die1}")
        print(f"Roll : Die 2 rolled a {die2}")
        print(f"Roll : Die 3 rolled a {die3}")
        sum1 = die1 + die2 + die3
        print("Total Dies is",{sum1})    
    else:
        print("Invalid Input. Please type 'Start' to begin the game.")

main()

