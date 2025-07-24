import time
import re

def is_english_hebrew_valid_name(name):
    if not name:
        print("Error: Name cannot be empty!")
        return False
    if re.match(r'^[\u0590-\u05FFa-zA-Z\s-]+$', name):
        return True
    print("Error: Name should contain only Hebrew or English letters, spaces, or hyphens!")
    return False

def get_valid_name():
    while True:
        name = input("Welcome to my final project\nWhat is your name? ").strip()
        if is_english_hebrew_valid_name(name):
            return name

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer!")

def isEven(num):
    return num % 2 == 0 

def getEvenOdd(num):
    return "even" if isEven(num) else "odd"

def is_valid_operator(operator):
    return operator in ["+", "-", "*", "/"]

def get_valid_operator():
    while True:
        operator = input("Please choose an operator (+, -, *, /): ").strip()
        if is_valid_operator(operator):
            return operator
        print(f"Error: Operator '{operator}' is not supported, please enter a valid operator (+, -, *, /)!")

def calculate(num_1, num_2, operator):
    if operator == "+":
        return num_1 + num_2, True
    elif operator == "-":
        return num_1 - num_2, True
    elif operator == "*":
        return num_1 * num_2, True
    elif operator == "/":
        if num_2 == 0:
            print("Error: You can't divide by zero!")
            return None, False
        while True:
            ans = input("You chose division, should the result be integer? (y/n): ").lower()
            if ans in ["y", "n"]:
                break
            print("Error: Please enter 'y' or 'n'!")
        if ans == "y":
            return num_1 // num_2, True
        return num_1 / num_2, True

name = get_valid_name()

print(f"Hi {name}, nice to meet you!\nThis is a special calculator, I need two numbers from you.")

num_1 = get_integer_input("Type in your first number: ")
num_2 = get_integer_input("Type in your second number: ")

type_1 = getEvenOdd(num_1)
type_2 = getEvenOdd(num_2)

print(f"Thank you for entering {num_1} and {num_2}.\nThe first number is {type_1} and the second is {type_2}.")

if type_1 == type_2:
    print(f"So both of them are {type_1}.")
else:
    print(f"So one of them is {type_1}, and one is {type_2}.")

operator = get_valid_operator()

result, is_valid = calculate(num_1, num_2, operator)
if is_valid:
    print(f"{num_1} {operator} {num_2} = {result}")

now = time.ctime()
print(f"Thank you {name} for using the calculator on {now}.")