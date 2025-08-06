nums = [[9,8,7],[6,5,4],[3,2,1]]
rows = len(nums)
cols = len(nums[0])
for i in range(0,rows):
    for j in range(0,cols):
        if i+j == rows-1:
            print(nums[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()