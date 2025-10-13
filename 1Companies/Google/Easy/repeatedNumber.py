class Solution:
    def repeatedNumber(self, A):
        freq = {}
        for i in range(len(A)):
            if A[i] not in freq:
                freq[A[i]] = 1
            else:
                freq[A[i]] += 1
        
        for k,v in freq.items():
            if v > 1:
                return k
                break
        return -1

A = list(map(int,input().split()))
print(Solution().repeatedNumber(A))
