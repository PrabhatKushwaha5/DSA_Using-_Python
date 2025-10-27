class Solution:
    def setZeroes(self, A):
        if not A:
            return A
        
        rows = len(A)
        cols = len(A[0])
        zero_rows = set()
        zero_cols = set()
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)


        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    A[i][j] = 0
        return A
matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]

print("Original Matrix:")
for row in matrix:
    print(row)

# Create object and call function
obj = Solution()
result = obj.setZeroes(matrix)

print("\nMatrix After Setting Zeroes:")
for row in result:
    print(row)