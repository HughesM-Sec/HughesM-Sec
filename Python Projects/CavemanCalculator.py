# Numbers Project: Simple Calculator
# Build a basic calculator that:
# Asks the user for two numbers
# Allows the user to choose an operation
# (addition, subtraction, multiplication, division)
# Performs the calculation and displays the result
# Handles division by zero gracefully
# Optionally: Include more advanced operations like exponentiation or square root

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter one of the following operators, +, -, *, /: ")

if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 != 0: # Originally I had if num2 != '0'
        # but that was comparing a float to a string
        # so removing the '' necessary because a float
        # will never be equal to a string.
        result = num1 / num2
        print(result)
    else:
        print("Cannot divide by zero.")
else:
    print("Not a valid selection.")
