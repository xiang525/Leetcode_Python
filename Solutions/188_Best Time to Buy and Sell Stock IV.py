class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        if len(prices) < 1:
            return 0
        low = prices[0]
        high = prices[0]
        profit = []
        for i in range(len(prices)):
            if prices[i]>=high:
                high = prices[i]
            else:
                profit.append(high-low)
                low = prices[i]
                high = prices[i]
        profit.append(high-low)
        print profit
        profit = sorted(profit, reverse=True)
        return sum(profit[:k])

s = Solution()
print s.maxProfit(2, [1,2,4,2,5,7,2,4,9,0])