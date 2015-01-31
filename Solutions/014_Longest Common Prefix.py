class Solution:

    def longestCommonPrefix(self, strs):
        "Given a list of pathnames, returns the longest common leading component"
        if not strs:
            return ''
        s1 = min(strs)
        s2 = max(strs)
        print s1, s2
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


    # def longestCommonPrefix(self, strs):
    #     if len(strs) == 0:
    #         return ""
    #     longest = strs[0]
    #     for str in strs[1:]:
    #         i = 0
    #         while i < len(str) and i < len(longest) and str[i] == longest[i]:
    #             i += 1
    #         longest = longest[:i]
    #     return longest
