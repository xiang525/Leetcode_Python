class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        l = len(s)
        for i in range(l):
            res += 26**i*(ord(s[l-i-1]) - 64)
        return res