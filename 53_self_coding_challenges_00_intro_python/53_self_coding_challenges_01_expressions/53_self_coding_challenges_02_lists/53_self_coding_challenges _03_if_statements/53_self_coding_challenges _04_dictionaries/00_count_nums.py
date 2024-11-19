# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
def number():
    print("To Stop press Enter to 'finish'")   
    user_dict ={}
    while True:
        user_input = input("Enter a number").lower()
        if user_input == '':
            break
        try:
            num =int(user_input)
            if num in user_dict:
                user_dict[num]+=1
            else:
                user_dict[num]=1
        except IndexError:
            print("Please enter valid number or 'stop' to end ")

    for number , count in user_dict.items():
        print(f"{number} appear {count} time")        
number()

