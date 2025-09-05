def calculator():
    print("Selection Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Remainder")

    choice = input("Enter your choice (1-6): ")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
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
    else:
        print("Invalid choice. Please select a number from 1 to 6.")

# Run the calculator
calculator()
