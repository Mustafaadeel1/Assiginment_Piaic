# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Here's a sample run of the program (user input is in blue):
AFFIRMATION = "I am capable of doing anything I put my mind to."

def sentence():
    user_in = input("Write the Affirmation :").strip().lower()
    if user_in != AFFIRMATION.lower():  
        print("Nice Work keep it up")  
    else:
        print("This is not AFFIRMATION")

sentence()
