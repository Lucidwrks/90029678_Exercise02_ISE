# This is a dodgy calculator

# function to multiply or divide
def times_or_divide(operation):
    global num_one, num_two
    # choose operation
    if operation == "*":
        return num_one * num_two
    elif operation == "/":
        return num_one / num_two
    else:
        raise ValueError("Invalid operation")
    
# function to add or subtract
def add_or_subtract(operation):
    global num_one, num_two
    # choose operation
    if operation == "+":
        return num_one + num_two
    elif operation == "-":
        return num_one - num_two
    else:
        raise ValueError("Invalid operation")
    
def get_number():
    # This loops until the user enters a valid number
    while True:
        try:
            global number
            number = float(input())
            break
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    # get the first number
    get_number()
    num_one = number

    # get the operation
    operation = input()

    # get the second number
    get_number()
    num_two = number

    # choose operation
    if operation == "*" or operation == "/":
        print(times_or_divide(operation))
    elif operation == "+" or operation == "-":
        print(add_or_subtract(operation))
    else:
        print("Invalid input")

    # ask if the user wants to calculate again
    # I tried but I couldn't get this to work more than once :(
    print("Do you want to calculate again? (y/n)")
    if input() == "y":
        # get the first number
        get_number()
        num_one = number

        # get the operation
        operation = input()

        # get the second number
        get_number()
        num_two = number

        # choose operation
        if operation == "*" or operation == "/":
            print(times_or_divide(operation))
        elif operation == "+" or operation == "-":
            print(add_or_subtract(operation))
        else:
            print("Invalid input")
    else:
        print("Goodbye")