# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:
def even_num():
    two =2
    for i in range(20):
        print(f"{two * i} ",end ="")
even_num()
