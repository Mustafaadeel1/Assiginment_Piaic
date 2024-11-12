def age():
    user_age = int(input("Enter your age for voting (:"))
    if user_age >= 16:
        print("You are eligible to vote in the Peturksbouipo election:")
        if user_age >= 25:
            print("You are eligible to vote in the Stanlau election :")
            if user_age >= 48:
                print("You are eligible to vote in the Mayengua election :")
            else:
                print("You cannot vote in Mayenguawhere the voting age is 48.")
        else:
            print("You cannot vote in Stanlau the voting age is 25.")
    else:
        print("You cannot vote in Peturksbouipo the voting age is 16.")
age()
