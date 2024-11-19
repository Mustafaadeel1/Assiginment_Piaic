# Objective:
#Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.
def access_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return "Index out of range"

def modify_element(my_list, index, new_value):
    try:
        my_list[index] = new_value
        return f"Element at index {index} successfully updated to {new_value}"
    except IndexError:
        return "Index out of range"

def slice_list(my_list, start_index, end_index):
    try:
        return my_list[start_index:end_index]
    except (TypeError, ValueError):
        return "Invalid indices provided"

def game():
    # Initial list
    my_list = [10, 20, 30, 40, 50, 60, 70]
    print("Welcome to the List Interaction Game!")
    print(f"Current List: {my_list}")

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print(f"Result: {result}")

        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print(f"Result: {result}")
            print(f"Updated List: {my_list}")

        elif choice == "3":
            start_index = int(input("Enter the start index: "))
            end_index = int(input("Enter the end index: "))
            result = slice_list(my_list, start_index, end_index)
            print(f"Result: {result}")

        elif choice == "4":
            print("Thank you for playing! Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Start the game
game()
