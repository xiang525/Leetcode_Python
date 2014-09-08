class Solution:
    # @return a list of strings, [s1, s2]

    def letterCombinations(self, digits):
        lookup, res = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []
        self.letterCombinationsRecur(lookup, res, "", digits)
        return res

    def letterCombinationsRecur(self, lookup, res, current, digits):
        if digits == "":
            res.append(current)
            return
        for choice in lookup[int(digits[0])]:
            self.letterCombinationsRecur(lookup, res, current + choice, digits[1:])
