class Solution:
    # @param x, an integer
    # @return an integer

    def sqrt(self, x):
        if x == 0:
            return 0
        i = 1
        j = x / 2 + 1
        while(i <= j):
            center = (i + j) / 2
            if center ** 2 == x:
                return center
            elif center ** 2 > x:
                j = center - 1
            else:
                i = center + 1
        return j
