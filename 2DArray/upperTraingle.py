arr = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(arr)
cols = len(arr[0])
for i in range(0,rows):
    for j in range(0,cols):
        if j>=i:
            print(arr[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()