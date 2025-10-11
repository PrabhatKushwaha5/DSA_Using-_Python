class Solution(object):
    def subsets(self,nums):
        result = []

        def func(index,subset):
            if index>=len(nums):
                result.append(list(subset))
                return 
            subset.append(nums[index])
            func(index+1,subset)
            subset.pop()
            func(index+1,subset)

        func(0,[])
        return result
    
nums = [1,2,3]
print(Solution().subsets(nums))