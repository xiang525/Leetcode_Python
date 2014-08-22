class Solution:
    # @return an integer

    def lengthOfLongestSubstring(self, s):
        substring = ""
        maxLength = 0
        maxString = ""
        for i in range(len(s)):
            substring += s[i]
            print i
            for j in range(i + 1, len(s)):
                if s[j] not in substring:
                    substring += str(s[j])
                    if len(substring) > maxLength:
                        maxLength = len(substring)
                        maxString = substring
                else:
                    if len(substring) > maxLength:
                        maxLength = len(substring)
                        maxString = substring
                    substring = ""
        print maxString
        return maxLength
