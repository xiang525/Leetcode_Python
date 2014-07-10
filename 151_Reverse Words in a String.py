# Note: Done
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if s.isspace():
            return ""
        else:
            sList = s.split()
            re = sList[::-1]
            return " ".join(re).strip
        
# Given an input string, reverse the string word by word.
# 
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".