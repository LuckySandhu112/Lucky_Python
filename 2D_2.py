A = [[1, 2, 3]]
B = [[4, 5, 6]]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Matrix:")
for row in result:
    print(row)