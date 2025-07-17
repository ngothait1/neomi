import time

def isEven(num):
    return num % 2 == 0 

def getEvenOdd(num):                       # לא התאפקתי לא להשתמש בפונקציה בכלל ובמקוננת
    return "even" if isEven(num) else "odd"

def calculate(num_1, num_2, operator):
    if operator == "+":
        return num_1 + num_2, True
    elif operator == "-":
        return num_1 - num_2, True
    elif operator == "*":
        return num_1 * num_2, True
    elif operator == "/":
        if num_2 == 0:
            return "You can't divide by zero", False
        ans = input("You chose division, should the result be integer? (y/n)")
        if ans == "y":
            return num_1 // num_2, True
        return num_1 / num_2, True
    else:
        return f"""Operator {operator} is not supported An error had occured, 
    please try again""", False

name = input("""Hello, This is my final project
What is your name? """)

print(f"""Hi {name}, nice to meet you
This is a special calculator, I would need two numbers from you""")

num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))

type_1 = getEvenOdd(num_1)
type_2 = getEvenOdd(num_2)

print(f"""Thank you for putting in your numbers, {num_1} and {num_2}
I can see that the first number is {type_1} And the second is {type_2}""")

if type_1 == type_2:
    print(f"So both of them are {type_1}")
else:
    print(f"So one of them is {type_1}, and one is {type_2}")

operator = input("Please choose an operator (+, -, *, /):")

result, is_valid = calculate(num_1, num_2, operator)

if is_valid:
    print(f"{num_1} {operator} {num_2} = {result}")

now = time.ctime()
print(f"Thank you {name} for using the calculator on {now}")

