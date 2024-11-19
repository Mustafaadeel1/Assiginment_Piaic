# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.
import random
def done():
    
    return random.randint(1, 100) <= 30

def chaotic_counting():
    for i in range(1, 11):
        if done(): 
            return
        print(i)  

def main():
    chaotic_counting()
    print("I am Done!")
     
main()
