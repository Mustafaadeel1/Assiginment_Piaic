# Print 10 random numbers in the range 1 to 100.
import random
def random_num():
    user_num = (input("To get random  number between 1 and 100, enter a number: ").lower())
    if user_num == "number":
        for i in range(10):
            print(random.randint(1,100))
    else:
         print("Invalid input")

random_num()