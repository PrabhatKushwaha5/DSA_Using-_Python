class Solution:
    def findUnion(self, a, b):
        # code here 
        freq = {}
        n = len(a)
        for i in range(n):
            if a[i] not in freq:
                freq[a[i]] = 1
            else:
                freq[a[i]] += 1
                
        m = len(b)
        for i in range(m):
            if b[i] not in freq:
                freq[b[i]] = 1
            else:
                freq[b[i]] += 1
        
        
        ans = []
        for k,v in freq.items():
            ans.append(k)
            
        
        return sorted(ans)

a = list(map(int,input().split()))
b = list(map(int,input().split()))
sol = Solution()
print(sol.findUnion(a,b))