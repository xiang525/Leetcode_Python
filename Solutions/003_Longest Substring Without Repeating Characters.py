class Solution:
    # @return an integer

    # def lengthOfLongestSubstring(self, s):
    #     substring = ""
    #     maxLength = 0
    #     maxString = ""
    #     for i in range(len(s)):
    #         substring += s[i]
    #         print i
    #         for j in range(i + 1, len(s)):
    #             if s[j] not in substring:
    #                 substring += str(s[j])
    #                 if len(substring) > maxLength:
    #                     maxLength = len(substring)
    #                     maxString = substring
    #             else:
    #                 if len(substring) > maxLength:
    #                     maxLength = len(substring)
    #                     maxString = substring
    #                 substring = ""
    #     print maxString
    #     return maxLength

    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for i in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == False:
                visited[ord(char)] = True
            else:
                while s[start] != char:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            longest = max(longest, i - start + 1)
        return longest
