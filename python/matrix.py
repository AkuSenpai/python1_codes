matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
rows=len(matrix)
cols=len(matrix[0])
transpose=[]
for i in range(cols):
    new_rows=[]
    for j in range(rows):
        new_rows.append(matrix[j][i])
    transpose.append(new_rows)
print("orignal matrix:")
for row in matrix:
    print(row)
print("transpose matrix:")
for row in transpose:
    print(row)

