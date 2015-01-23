class Solution:
    # @return a boolean

    def isPalindrome(self, x):
        if x < 0:
            return False
        divider = 1
        while(x / divider >= 10):
            divider *= 10
        while(x != 0):
            left = x / divider
            right = x % 10
            if left != right:
                return False
            x %= divider
            x /= 10
            divider /= 100
        return True

    # def isPalindrome(self, x):
    #     if str(x).startswith("-"):
    #         return False
    #     y = str(x)[::-1]
    #     res = True if y == y[::-1] else False
    #     return res
