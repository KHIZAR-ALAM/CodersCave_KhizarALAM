#funtions of operaters
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
# taking user input 
while True:
    print("===========CALCULATOR==============")
    print("Options:")
    print("Enter 'ADD' for addition")
    print("Enter 'SUBTRACT' for subtraction")
    print("Enter 'MULTIPLY' for multiplication")
    print("Enter 'DIVIDE' for division")
    print("Enter 'QUIT' to end the program")
   #user input converted to lowercase 
    user_input = input(": ").lower()

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))
    #function call as per user input
        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ", divide(num1, num2))
    else:
        print("Invalid input")
