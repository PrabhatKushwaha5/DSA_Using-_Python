matrix = [[7,10,29,3],[1,20,0,4],[19,0,6,11],[4,27,14,7]]
r = len(matrix)
c = len(matrix[0])
rowtrack = [0 for _ in range(r)]
coltrack = [0 for _ in range(c)]
for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j] == 0:
            rowtrack[i] = -1
            coltrack[j] = -1

for i in range(r):
    for j in range(c):
        if rowtrack[i] == -1 or coltrack[j] == -1:
            matrix[i][j] = 0
print(matrix)