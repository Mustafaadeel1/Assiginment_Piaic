#There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!
def adult_age(x):
    if x >= 18:
        print("Entered age is an adult age")
        print(f"You are an adult {x}")
        True
    else:
        print("Entered age is not an adult age")
        print(f"You are not an adult {x}")
        False
age = int(input("Enter your age: "))
adult_age(age)
