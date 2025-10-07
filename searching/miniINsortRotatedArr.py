class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 0
        h = n-1
        mini = float("inf")
        while l<=h:
            m = (l+h)//2
            if nums[m]<=nums[h]:
                mini = min(mini,nums[m])
                h = m-1
            else:
                mini = min(mini,nums[l])
                l = m+1
        return mini
        

nums = list(map(int,input().split()))
sol = Solution()
print(sol.findMin(nums))