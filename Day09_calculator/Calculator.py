
# Define the functions for operations
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error! Division by zero."


# Dictionary mapping operation symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Main calculator function
def calculator():
    print(r""" _____________________
    |  _________________  |
    | | krish_cal     0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|""")

    print("\nWelcome to the Calculator!")

    num1 = float(input("What's the first number? "))

    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above: ")
        if operation_symbol in operations:
            num2 = float(input("What's the next number? "))

            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

            if choice == 'y':
                num1 = answer
            else:
                should_continue = False
                print("\nStarting a new calculation...\n")
                calculator()  # Restart the calculator
        else:
            print("invalid symbol, try again")


# Start the calculator
calculator()
