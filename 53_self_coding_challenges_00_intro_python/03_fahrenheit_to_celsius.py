# Temperature in Celsius
temperature = input("Enter your Temperature in Fahrenheit -> ")
fahrenheit = float(temperature)
celsius = (fahrenheit - 32) * 5 / 9
print(f"The temperature {temperature}°F in Celsius is {celsius:.2f}°C")
