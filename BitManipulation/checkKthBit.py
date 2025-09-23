class Solution:
    def checkKthBit(self, n, k):
        # code here
        return (n & (1<<k)) != 0
    
n = int(input())
k = int(input())
obj = Solution()
print(obj.checkKthBit(n,k))