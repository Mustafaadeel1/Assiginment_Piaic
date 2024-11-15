# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
def countdown():
    for i in range(1,10 +1):
        print(i,end=" ")
    print("Liftoff")
countdown()