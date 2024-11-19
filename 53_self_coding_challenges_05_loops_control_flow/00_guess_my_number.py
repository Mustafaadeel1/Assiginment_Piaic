# Guess My Number
import random
def guess_number():
    user_num = int (input("I am thinking of a number between 0 and 99..."))
    computer_num = random.randint(0, 99)
    if user_num == computer_num:
        print(f" Congrats! The number was:{computer_num}")
    elif user_num < computer_num:
            print(f"Your guess:{user_num} is too low My guess is this:{computer_num}")
    elif user_num > computer_num:
                print(f"Your guess:{user_num}  is too high  My guess is this:{computer_num}")
    else:        
        print("Please Enter valid number")
guess_number()