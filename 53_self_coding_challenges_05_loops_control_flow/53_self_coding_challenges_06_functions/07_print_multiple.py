# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.
def num_multiply():
    user_mess = input("please type aa message :")
    user_num = int(input("Enter a number of times to repeat your message: "))
    total =" ".join([user_mess] * user_num)
    print(total)
num_multiply()