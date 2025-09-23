class Solution:
    def isEven (self, n):
        # code here 
        return (n&1) == 0
    

n = int(input())
obj = Solution()
print(obj.isEven(n))