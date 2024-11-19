# # Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.
def joke(user):
    if user == "joke":
        print("Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why, and Sophia replies: 'because they had eggs.'")
    else:
        print("Sorry, I only tell jokes.")

user_joke = input("What do you want? ").lower().strip()
joke(user_joke)
