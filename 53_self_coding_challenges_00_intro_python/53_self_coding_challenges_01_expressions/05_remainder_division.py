# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
user_div = input("Please enter an integer to be divided ->:")
user_to = input("Please enter an integer to divide by ->:")
div_result = int(user_div) // int(user_to)
modu_result = int(user_div) % int(user_to)
print(f"The result of this division is {div_result} with a remainder of {modu_result} ")
