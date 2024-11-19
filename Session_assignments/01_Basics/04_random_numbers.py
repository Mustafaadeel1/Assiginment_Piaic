# Print 10 random numbers in the range 1 to 100.
# Each time you run your program you should get different numbers
import random
def print_random_numbers():
    for i in range(10):
        print(random.randint(1, 100),end=" ")

print_random_numbers()
