def square_pattern():
    side = int(input("Enter the value of side: "))
    for i in range(side):
        for j in range(side):
            print('*', end=' ')
        print()

def rectangle_pattern():
    row = int(input("Enter the number of rows: "))
    column = int(input("Enter the number of columns: "))
    for i in range(row):
        for j in range(column):
            print('*', end=' ')
        print()

def triangle_pattern():
    rows = int(input("Enter the number of rows: "))
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end=' ')
        print()

while True:
    print("\n--- Pattern Menu ---")
    print("1. Square Pattern")
    print("2. Rectangle Pattern")
    print("3. Triangle Pattern")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        square_pattern()
    elif choice == '2':
        rectangle_pattern()
    elif choice == '3':
        triangle_pattern()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
