class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        buy = float("inf")
        sell = 0
        for i in range(n):
            buy = min(buy,prices[i])
            sell = max(sell,prices[i]-buy)
        return sell
    
prices = list(map(int,input().split()))
sol = Solution()
print(sol.maxProfit(prices))




#[7,1,5,3,6,4]