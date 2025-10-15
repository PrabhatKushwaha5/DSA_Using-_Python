class Solution:
    def SpiralMatrix(self, A):
        result = []
        top = 0
        bottom = len(A) - 1
        left = 0
        right = len(A[0]) - 1

        while top <= bottom and left <= right:
            
            for i in range(left, right + 1):
                result.append(A[top][i])
            top += 1

            
            for i in range(top, bottom + 1):
                result.append(A[i][right])
            right -= 1

            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(A[bottom][i])
                bottom -= 1

            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(A[i][left])
                left += 1  

        return result


# ---------- Input from user ----------
rows, cols = map(int, input("Enter rows and columns: ").split())
A = []
for i in range(rows):
    A.append(list(map(int, input().split())))


print(Solution().SpiralMatrix(A))
