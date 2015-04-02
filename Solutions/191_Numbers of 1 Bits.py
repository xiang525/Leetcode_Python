class Solution:
    # @param n, an integer
    # @return an integer

    def hammingWeight(self, n):
        # return bin(n)[2:].count('1')
        # Bit Manuplation, the performance is worse than string operation
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans

s = Solution()
print s.hammingWeight(3)
