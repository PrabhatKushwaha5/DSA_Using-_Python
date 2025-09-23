class Solution:
    def isPalindrome(self, s):
        # code here
        front = 0
        n = len(s)
        last = n-1
        while front <= last:
            if s[front] != s[last]:
                return False
                break
            else:
                front += 1
                last -= 1
        return True
    
s = input().strip()
obj  = Solution()
print(obj.isPalindrome(s))