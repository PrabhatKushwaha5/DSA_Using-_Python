class Solution:
    
    def twoSum(self, A, B):
        seen = {}  
        for i, num in enumerate(A):
            complement = B - num
            if complement in seen:
                
                return [seen[complement] + 1, i + 1]
            if num not in seen:
                seen[num] = i  
        return []

A = list(map(int, input("Enter numbers separated by space: ").split()))
B = int(input("Enter target: "))

print(Solution().twoSum(A,B))
