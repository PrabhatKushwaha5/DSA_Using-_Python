

class Solution:
    def sumOfSeries(self, n):
        
        if n == 0:
            return 0
        
        
        return n**3 + self.sumOfSeries(n-1)

if __name__ == "__main__":
    n = int(input("Enter n: "))
    ob = Solution()
    print(ob.sumOfSeries(n))
