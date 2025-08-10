class Solution:
    def arranged(self, arr):
        # Separate positives and negatives while keeping order
        pos = [num for num in arr if num >= 0]
        neg = [num for num in arr if num < 0]
        
        # Merge them alternately
        res = []
        for p, n in zip(pos, neg):
            res.append(p)
            res.append(n)
        
        return res


# Input
arr = list(map(int, input().split()))

# Create object and call method
sol = Solution()
result = sol.arranged(arr)

# Output
print(result)
