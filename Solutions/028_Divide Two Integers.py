class Solution:
    # @return an integer

    def divide(self, dividend, divisor):
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        summing = 0
        count = 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            summing = b
            count = 1
            while summing + summing <= a:
                summing += summing
                count += count
            a -= summing
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res
