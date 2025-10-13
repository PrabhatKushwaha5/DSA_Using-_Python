class Solution:
    
    def solve(self, A):
        maxx = float("-inf")
        minn = float("inf")
        for i in range(len(A)):
            maxx = max(maxx,A[i])
            minn = min(minn,A[i])
        return maxx+minn
    
A = list(map(int,input().split()))
print(Solution().solve(A))
