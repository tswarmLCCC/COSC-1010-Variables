

user_input = float(input("Enter temperature in Farenheit: "))
converted_fahrenheit = (user_input - 32) * 5/9
print(f"{user_input}°F is {converted_fahrenheit:.2f}°C")


celsius = float(input("Enter temperature in celsius: "))
converted_fahrenheit = (celsius * 9/5) + 32
print(f"{user_input}°C is {converted_fahrenheit:.2f}°F")
