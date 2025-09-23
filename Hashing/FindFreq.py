class Solution:
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        freq = {}
        for i in range(1,n+1):
            freq[i] = 0
            
        for i in range(n):
            if arr[i] in freq:
                freq[arr[i]] += 1
                
        res = []
        for i in range(1,n+1):
            res.append(freq[i])
        return res

arr = list(map(int,input().split()))
obj = Solution()
print(obj.frequencyCount(arr))