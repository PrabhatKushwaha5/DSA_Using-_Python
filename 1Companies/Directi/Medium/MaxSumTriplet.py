class Solution:
    def solve(self,A):

        n = len(A)
        ans = 0

        for j in range(1,n-1):

            leftMax = 0
            rightMax = 0

            for i in range(j):
                if A[i]<A[j]:
                    leftMax = max(leftMax,A[i])

            for k in range(j+1,n):
                if A[k] > A[j]:
                    rightMax = max(rightMax,A[k])

            if leftMax > 0 and rightMax > 0:
                ans = max(ans,leftMax + A[j] + rightMax)
        return ans
    

A = list(map(int,input().split()))
sol = Solution()
print(sol.solve(A))
