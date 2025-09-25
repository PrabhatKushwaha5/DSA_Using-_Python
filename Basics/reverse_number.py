class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_min = -2**31
        int_max = 2**31-1

        res = 0
        sign = -1 if x<0 else 1
        x = abs(x)

        while x != 0:
            digit = x%10
            x //= 10

            if (res>int_max//10) or (res == int_max // 10 and digit > int_max % 10):
                return 0
            
            res = res*10 + digit
        return sign*res
    
x = int(input("Enter an integer: "))
s = Solution()
result = s.reverse(x)
print("Reversed integer:", s.reverse(x))