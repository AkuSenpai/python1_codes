import math

def calculator():
    print("Selection Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Remainder")
    print("7. Logarithm (base 10)")
    print("8. Square Root")

    choice = input("Enter your choice (1-8): ")

    try:
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        elif choice == '7':
            num = float(input("Enter the number for logarithm (base 10): "))
        elif choice == '8':
            num = float(input("Enter the number for square root: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    elif choice == '5':
        if num2 != 0:
            print("Result:", num1 // num2)
        else:
            print("Error: Cannot divide by zero.")
    elif choice == '6':
        if num2 != 0:
            print("Result:", num1 % num2)
        else:
            print("Error: Cannot find remainder with divisor zero.")
    elif choice == '7':
        if num > 0:
            print("Result:", math.log10(num))
        else:
            print("Error: Logarithm undefined for non-positive numbers.")
    elif choice == '8':
        if num >= 0:
            print("Result:", math.sqrt(num))
        else:
            print("Error: Square root undefined for negative numbers.")
    else:
        print("Invalid choice. Please select a number from 1 to 8.")

# Run the calculator
calculator()
