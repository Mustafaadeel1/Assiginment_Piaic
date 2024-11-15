# Hi : My name is Mustafa.
__My age is 17 year old__
* I am piaic Qutar 1 student.  
* I live in sialkot.
### Python Programming Assignment: Number Exploration Tool.
**Instructions:**
 
 1.  First you say user enter your name. 
``` 
name = str (input("Enter your name:"))
```
 2. Ask him give me your three favorite number. 
``` 
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))
``` 

 3. You print a message to user call his name and beautiful message  send let`s check your three favorite number.
 ```
 print(f"\nHello, {name}! Let's explore your favorite numbers:")
 ```
 4. You check the number is "even" or "odd" if number is even "you   
 say this number is even &  number is odd you say this number is odd 
 store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd".
 ```
 if num1 % 2 == 0:
    print(f"The number {num1} is even.")
else:
    print(f"The number {num1} is odd.")
```
 5.  This program should use a for loop to iterate over the list of numbers, and for each number, it should create a tuple containing the number and its square.
 ```
 print(f"The number {num1} and its square: ({num1}, {num1 ** 2})")
 ```
 6. These tuples should be printed in a creative and engaging format. Additionally, the program should calculate the sum of the three numbers and print the result, accompanied by an encouraging message.
 ```
 otal_sum = num1 + num2 + num3
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
```

 7.  Finally, the program should determine if the sum is a prime number and notify the user with an appropriate message.
 ```
 if total_sum < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(total_sum **2) ):
        if total_sum % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")
```

__This is my short game__

__Thanks To read it__
[Exploration Tool Question ](https://github.com/JahanzaibTayyab/Batch-62/blob/main/python-learning/assignments/Number_Exploration_Tool.md)

[Exploration Tool Solution](https://github.com/Mustafaadeel1/My-Assignment/blob/main/game.py)
 