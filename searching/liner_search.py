class Solution:
    def search(self, arr, x):
        # code here
        n = len(arr)
        ans = -1
        for i in range(n):
            if arr[i] == x:
                ans = i
                break
        return ans
    
arr = list(map(int,input().split()))
x = int(input())
sol = Solution()
print(sol.search(arr,x))