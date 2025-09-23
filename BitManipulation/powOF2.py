class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (n&(n-1)) == 0
    
n = int(input())
obj = Solution()
print(obj.isPowerOfTwo(n))