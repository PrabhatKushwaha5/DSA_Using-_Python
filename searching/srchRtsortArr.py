class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        result =  0
        for i in range(0,n):
            if nums[i] == target:
                result = i
                break
            else:
                result = -1
        return result

        
nums = list(map(int,input().split()))
target = int(input())
sol = Solution()
print(sol.search(nums,target))