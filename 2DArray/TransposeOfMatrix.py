nums = [[6,5,4],[3,2,1]]
rows = len(nums)
cols = len(nums[0])
result = [[0]*rows for _ in range(cols)]
for i in range(0,rows):
    for j in range(0,cols):
        result[j][i] = nums[i][j]
print(result)