class Solution:
    # @param n, an integer
    # @return an integer

    def hammingWeight(self, n):
        return bin(n)[2:].count('1')


s = Solution()

print s.hammingWeight(1100)
