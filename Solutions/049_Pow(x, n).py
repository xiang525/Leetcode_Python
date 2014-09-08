class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

    def pow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2:
            return pow(x * x, n / 2) * x
        else:
            return pow(x * x, n / 2)
