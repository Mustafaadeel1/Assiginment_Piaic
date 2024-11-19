# Initialize an empty list globally
li = []

def count_even():
    while True:  # Keep asking for input until the user presses Enter without input
        user_input = (input("Enter an integer or press enter to stop: "))
        
        if user_input == "":  # Exit the loop if input is empty
            break
        
        user = int(user_input)  # Convert the input to an integer
        
        if user % 2 == 0:  # Check if the number is even
            li.append(user)  # Append the even number to the list
    
    return li  # Return the list after the loop

print(count_even())  # Call the function and print the result
