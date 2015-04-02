class Solution:
    # @return an integer as the maximum profit 
    # def maxProfit(self, k, prices):
        # if len(prices) < 1:
        #     return 0
        # low = prices[0]
        # high = prices[0]
        # profit = []
        # for i in range(len(prices)):
        #     if prices[i]>=high:
        #         high = prices[i]
        #     else:
        #         profit.append(high-low)
        #         low = prices[i]
        #         high = prices[i]
        # profit.append(high-low)
        # print profit
        # profit = sorted(profit, reverse=True)
        # return sum(profit[:k])
        # 

    def maxProfit(self, k, prices):
        size = len(prices)
        if k > size / 2:
            return self.quickSolve(size, prices)
        dp = [None] * (2 * k + 1)
        dp[0] = 0
        for i in range(size):
            for j in range(min(2 * k, i + 1) , 0 , -1):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
        return max(dp)

    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum

s = Solution()
print s.maxProfit(2, [1,2,4,2,5,7,2,4,9,0])