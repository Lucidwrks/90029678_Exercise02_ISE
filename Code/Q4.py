# This is a dodgy calculator (Not anymore)

######## 01. no more global variable. decrease coupling ########

######## 02. made all operations seperate functions to increase cohesion and decrease coupling ########
# Function to multiply
def times(operation, num_one, num_two):
    if operation == "*":
        return num_one * num_two
    else:
        raise ValueError("Invalid operation")
    
# Function divide
def divide(operation, num_one, num_two):
    if operation == "/":
        return num_one / num_two
    else:
        raise ValueError("Invalid operation")
    
# Function to add
def add(operation, num_one, num_two):
    if operation == "+":
        return num_one + num_two
    else:
        raise ValueError("Invalid operation")

# Function to subtract
def subtract(operation, num_one, num_two):
    if operation == "-":
        return num_one - num_two
    else:
        raise ValueError("Invalid operation")

def get_number():
    while True:
        try:
            number = float(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input")


######## 03. fix rededundancy issue by creating independant calc function  ########
def calculate():
    num_one = get_number()
    operation = input("Enter an operation (+, -, *, /): ")
    num_two = get_number()

    if operation in ["*"]:
        result = times(operation, num_one, num_two)
    elif operation in ["/"]:
        result = divide(operation, num_one, num_two)
    elif operation in ["+"]:
        result = add(operation, num_one, num_two)
    elif operation in ["-"]:
        result = subtract(operation, num_one, num_two)
    else:
        print("Invalid input")
        return

    print("Result:", result)

######## 03. fix rededundancy issue by only making code for asking user to continue occur once in a loop once answer is calculated. ########
    return input("Do you want to calculate again? (y/n)")

if __name__ == "__main__":
    repeat = "y"
    while repeat.lower() == "y":
        repeat = calculate()

    print("Goodbye")
