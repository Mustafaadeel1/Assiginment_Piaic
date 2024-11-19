# # Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result
def double():
    user = int(input("Enter a number to double: "))  # Get user input and convert it to an integer
    return user * 2  # Return the doubled value

# Calling the function and printing the result
print(double()) 