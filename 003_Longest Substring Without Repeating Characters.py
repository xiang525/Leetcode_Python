# Note:
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        substring = ""
        maxLength = 0
        maxString = ""
        for i in range(len(s)):
            substring += s[i]
            print i
            for j in range(i+1, len(s)):
#                 print substring
#                 print j
#                 print s[j], substring
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


# Given a string, find the length of the longest substring without repeating 
# characters. For example, the longest substring without repeating letters 
# for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest 
# substring is "b", with the length of 1.

s = Solution()
print s.lengthOfLongestSubstring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco")