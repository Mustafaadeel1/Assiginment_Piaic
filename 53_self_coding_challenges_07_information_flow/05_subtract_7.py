# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.
# Helper function to subtract 7
def subtract_seven(num):
    return num - 7

def main():
    num = int(input("Enter a number: "))
    
    result = subtract_seven(num)

    print(f"The result after subtracting 7 is: {result}")

main()
 