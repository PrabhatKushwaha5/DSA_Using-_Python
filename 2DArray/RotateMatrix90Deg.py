matrix = [[7,10,29,3],[1,20,0,4],[19,0,6,11],[4,27,14,7]]
r = len(matrix)
c = len(matrix[0])
for i in range(0,r):
    for j in range(0,c):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

for i in range(0,r):
    matrix[i].reverse()
print(matrix)
