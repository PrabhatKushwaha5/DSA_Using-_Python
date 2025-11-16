class Solution:
    def RotateMat(self,A):

        n = len(A)
        for i in range(n):
            for j in range(i+1,n):
                A[i][j],A[j][i] = A[j][i],A[i][j]

        

        for i in range(n):
            A[i].reverse()
        

        return A
    


A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

sol = Solution()
print(sol.RotateMat(A))