class Solution:
    def findFrequency(self, arr, x):
        # code here
        freq = {}
        n = len(arr)
        for i in range(n):
            if arr[i] not in freq:
                freq[arr[i]] = 1
            else:
                freq[arr[i]] += 1
        
        
        count = 0
        for k,v in freq.items():
            if k == x:
                return v
        return 0
    
n = int(input().strip())
arr = list(map(int,input().split()))
x = int(input())
obj = Solution()
print(obj.findFrequency(arr,x))