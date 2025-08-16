class Solution:
    def lower_bound(self,nums, target):
        n = len(nums)
        lb = -1
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    def upper_bound(self,nums, target):
        n = len(nums)
        ub = -1
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:   
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
    
    def first_and_last(self,nums,target):
        first = self.lower_bound(nums,target)
        last = self.upper_bound(nums,target)-1
        if first == -1 or first>=len(nums) or nums[first] != target:
            return [-1,-1]
        return [first,last]


nums = [1, 2, 3, 3, 3, 4, 5, 7]
target = 3

sol = Solution()
print(sol.first_and_last(nums, target))