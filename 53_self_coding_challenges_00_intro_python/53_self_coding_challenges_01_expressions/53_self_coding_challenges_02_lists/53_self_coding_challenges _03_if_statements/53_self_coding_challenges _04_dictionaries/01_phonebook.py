def read_phone_numbers():
    """
    Ask the user for names and phone numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}

    while True:
        name = input("Enter name (or press Enter to finish): ")
        if name == "":  # Exit loop if no name is entered
            break
        number = input("Enter number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints all names and phone numbers in the phonebook.
    """
    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allows user to look up numbers by name in the phonebook.
    """
    while True:
        name = input("Enter name to look up (or press Enter to finish): ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    # Read phone numbers into phonebook
    phonebook = read_phone_numbers()
    # Print all phonebook entries
    print_phonebook(phonebook)
    # Look up numbers
    lookup_numbers(phonebook)


# Run the main function
main()
