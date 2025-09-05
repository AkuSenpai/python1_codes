#patter programming of square
side=int(input("Enter the value of row:"))
for i in range(side):
    for j in range(side):
        print('*', end=' ')
    print()
#pattern programming of rectangle
row=int(input("Enter the value of row:"))
column=int(input("Enter the value of column:"))
for i in range(row):
    for j in range(column):
        print('*', end=' ')
    print()
#pattern programming of triangle
rows=int(input("Enter the value of row:"))
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()