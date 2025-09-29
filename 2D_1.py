list1 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

total = 0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        total = total + list1[i][j]

print("All elements: ", total)