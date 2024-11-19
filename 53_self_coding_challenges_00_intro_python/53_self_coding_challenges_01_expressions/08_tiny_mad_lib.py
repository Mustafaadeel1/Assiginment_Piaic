# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
print("Mad Libs Lets  Play! Fill the  blanks : ")
user_in = input("fill this word ti__")
if "tiny" == user_in:
    print("Next Blank fill")
    user_in1 = input("fill this word pla__")
    if  "plant" == user_in1:
        print("Answer Third And Last Blank")
        user_in2 = input("fill this word fl_")
        if "fly" == user_in2:
            print("Congratulations  You Won!")
        else:
            print("Sorry  You Lost! Because  you didn't fill the blanks correctly!")
    else:
        print("Sorry  You Lost! Because  you didn't fill the blanks correctly!")
else:
    print("Sorry  You Lost! Because  you didn't fill the blanks correctly!")

        




