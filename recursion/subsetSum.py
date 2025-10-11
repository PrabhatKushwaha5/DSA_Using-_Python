class Solution(object):
    def subSequenceSum(self,nums,k):

        result = []




        def solve(index,total,subset):
            if index == len(nums):
                if total == k:
                    result.append(list(subset))
                return
            
            subset.append(nums[index])
            solve(index+1,total+nums[index],subset)
            subset.pop()
            solve(index+1,total,subset)

        solve(0,0,[])
        return result


nums = [1,2,3,4,5,6,7,8]
k = 7
print(Solution().subSequenceSum(nums,k))