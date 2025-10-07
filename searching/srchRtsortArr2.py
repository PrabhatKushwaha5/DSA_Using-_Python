class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        l = 0
        h = n-1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                return True
            if nums[l] == nums[m] == nums[h]:
                l = l+1
                h = h-1
                continue
            if nums[m]<= nums[h]:
                if nums[m] <= target <= nums[h]:
                    l = m+1
                else:
                    h = m-1
            else:
                if nums[m]>= target >= nums[l]:
                    h = m-1
                else:
                    l = m+1
        return False
    
nums = list(map(int,input().split()))
target = int(input())
sol = Solution()
print(sol.search(nums,target))