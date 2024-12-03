# Modify
# This program takes user input and performs simple calculations

# Get user input
user_input = input("Enter two numbers separated by a space: ")

# Split user input into two numbers
num1, num2 = user_input.split()

# Convert numbers to integers
num1 = int(num1)
num2 = int(num2)

# Perform calculations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Display results
print("Sum: " + str(sum))
print("Difference: " + str(difference))
print("Product: " + str(product))
print("Quotient: " + str(quotient))
