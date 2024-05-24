#Implement a program that takes user input for a filename, opens the file in read mode, and displays its contents. 
# Handle the FileNotFoundError and display an error message if the file is not foun
try:
    filename = input("Enter the filename: ")
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

#Write a Python program that takes two integers as input and performs division (num1 / num2). 
# Handle both ValueError (if non-integer input) and ZeroDivisionError and display appropriate error messages.

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Write a Python program that takes user input for age. 
# Create a custom exception InvalidAgeError to handle cases where the age is below 0 or above 120. 
# Hint: Create new class InvalidAgeError that inherits Exception class


class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age entered.")
    print(f"Your age is: {age}")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Error: Invalid input. Please enter an integer for age.")
    
# Implement a program that reads user input for a password. Create a custom exception WeakPasswordError to handle cases where the password is shorter than 8 characters.
# Hint: WeakPasswordError that inherits Exception class

class WeakPasswordError(Exception):
    pass

try:
    password = input("Enter a password: ")
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long.")
    print("Password accepted.")
except WeakPasswordError as e:
    print(e)