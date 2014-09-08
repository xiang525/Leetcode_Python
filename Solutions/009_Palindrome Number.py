class Solution:
    # @return a boolean

    def isPalindrome(self, x):
        if str(x).startswith("-"):
            return False
        y = str(x)[::-1]
        res = True if y == y[::-1] else False
        return res
