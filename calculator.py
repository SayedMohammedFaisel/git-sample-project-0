# calculator.py

# Asks user for 2 operands and 1 operator
# Returns output of this operation

a = float(input("Enter number 1: "))  # Convert input to float
o = input("Enter operator: ")
b = float(input("Enter number 2: "))  # Convert input to float

if o in ['+', '-', '*', '/']:  # Removed [0] from o, not necessary
    if o == '+':
        out = a + b
    elif o == '-':
        out = a - b
    elif o == '*':
        out = a * b
    elif o == '/':
        if b != 0:  # Check for division by zero
            out = a / b
        else:
            print("Error: Division by zero!")
            exit()  # Exit the program if there's a division by zero
    print("Output: ", out)
else:
    print("Error: Invalid Operator")
