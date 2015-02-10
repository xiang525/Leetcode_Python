class Solution:
    # @param s, a string
    # @return a list of strings

    def findRepeatedDnaSequences(self, s):
        seq = {}
        res = []
        for i in range(len(s)):
            if s[i:i + 10] in seq:
                if s[i:i + 10] not in res:
                    res.append(s[i:i + 10])
            else:
                seq[s[i:i + 10]] = 1
        return res

s = Solution()
# print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print s.findRepeatedDnaSequences("AAAAAAAAAAAA")
