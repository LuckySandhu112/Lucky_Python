A = [[1,2,3],[4,5,6,]]
B = [[1,4],[2,5],[3,6]]

rows=len(A)
columns=len(A[0])

transpose =[]
for i in range(columns):
    new_rows=[]
    for j in range(rows):
        new_rows.append(A[j][i])
    transpose.append(new_rows)
print("transpose of matrix")
for row in transpose:
            print(row)