def arth(a,b):
    sum1=a+b
    sum2=a-b
    sum3=a*b
    sum4=a/b
    sum5=a//b
    sum6=a%b
    return 0
arth(a,b)
def calculator():
    print("Selection Options:-")
    print("1.Addition")
    print("2.Subraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Double Division")
    print("6.Reminder")

    choice=('''Enter 1.Addition,2.Subraction,3.Multiplication,
            4.Division,5.Double Divison,6.Reminder''')
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    if choice=='1':
        print(sum1)
    elif choice=='2':
        print(sum2)
    elif choice=='3':
        print(sum3)
    elif choice=='4':
        print(sum4)
    elif choice=='5':
        print(sum5)
    elif choice=='6':
        print(sum6)
    else:
        print("Invaild")
    return 0
calculator()
