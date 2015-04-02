class Solution:
    # @param num, a list of integer
    # @return an integer

    def rob(self, num):
        # Approach 1: Greedy algorithm: NOT CORRECT!!!
        # length = len(num)
        # if length == 0:
        #     return 0
        # elif length == 1:
        #     return num[0]

        # max_num = max(num)
        # max_index = num.index(max_num)
        # if max_index == 0:
        #     return max_num + self.rob(num[2:])
        # elif max_index == length - 1:
        #     return max_num + self.rob(num[:max_index-1])
        # else:
        #     return max_num + self.rob(num[:max_index-1] + num[max_index+2:])

        # Approach 2: sum of odd and even number: NOT CORRECT!!!
        # return max(sum(num[1::2]), sum(num[::2]))

        # Approach 3: Dynanmic programming
        length = len(num)
        dp = [0] * (length + 1)
        if length:
            dp[1] = num[0]
        for i in range(2, length + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
        print dp
        return dp[length]

s = Solution()
print s.rob([1, 1])
print s.rob([2, 3, 2])
print s.rob([2, 1, 1, 2])
print s.rob([0, 0, 0])
print s.rob([1, 7, 9, 4])
