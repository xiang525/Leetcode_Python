class Solution:
    # @return an integer

    def trailingZeroes(self, n):
        i = 1
        count = 0
        while n / (5 ** i) != 0:
            count += n / (5 ** i)
            i += 1
        return count