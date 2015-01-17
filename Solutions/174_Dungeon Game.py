class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer

    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for index in range(n)] for index in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for row in reversed(range(m - 1)):
            dp[row][n - 1] = max(1, dp[row + 1][n - 1] - dungeon[row][n - 1])
        for col in reversed(range(n - 1)):
            dp[m - 1][col] = max(1, dp[m - 1][col + 1] - dungeon[m - 1][col])
        for row in reversed(range(m - 1)):
            for col in reversed(range(n - 1)):
                dp[row][col] = max(
                    1, min(dp[row + 1][col], dp[row][col + 1]) - dungeon[row][col])
        return dp[0][0]
