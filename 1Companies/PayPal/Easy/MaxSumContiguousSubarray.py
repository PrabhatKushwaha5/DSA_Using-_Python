class Solution:
    def maxSum(self,A):
        max_sum = A[0]
        curr_sum = A[0]
        for i in range(1,len(A)):
            curr_sum = max(A[i],curr_sum + A[i])
            max_sum = max(curr_sum,max_sum)
        return max_sum
    
A = list(map(int,input("Enter list").split()))
print(Solution().maxSum(A))
