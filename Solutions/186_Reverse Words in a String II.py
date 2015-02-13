class Solution:

    """ return reversed works
    """
    def reverseWords(self, s):
        return " ".join(reversed(s.strip().split(" ")))

s = Solution()
print s.reverseWords("the sky is blue")
