# Simple Calculator with Interactive Session and Exit Keyword

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Welcome to the interactive calculator!")
print("Type 'exit' at any prompt to quit.\n")

while True:
    # Display available operations
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user choice
    choice = input("Enter choice (1/2/3/4): ")
    if choice.lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    # Get first number or exit
    num1_input = input("Enter first number: ")
    if num1_input.lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    # Get second number or exit
    num2_input = input("Enter second number: ")
    if num2_input.lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    # Convert inputs to float and handle invalid input
    try:
        num1 = float(num1_input)
        num2 = float(num2_input)
    except ValueError:
        print("Invalid number input. Please try again.\n")
        continue

    # Perform selected operation
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}\n")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}\n")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}\n")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}\n")
    else:
        print("Invalid operation choice. Please try again.\n")