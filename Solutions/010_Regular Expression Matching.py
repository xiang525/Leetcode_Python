class Solution:
    # @return a boolean

    def isMatch(self, s, p):
        previousRow = [True]
        for i in range(0, len(p)):
            if p[i] == '*':
                previousRow.append(previousRow[i - 1])
            else:
                previousRow.append(False)

        for letter in range(0, len(s)):
            actualRow = [False]
            for i in range(0, len(p)):
                if p[i] == '*':
                    temp = actualRow[i - 1] or (previousRow[i + 1] and (p[i - 1] == s[letter] or p[i - 1] == '.'))
                elif p[i] == '.':
                    temp = previousRow[i]
                else:
                    temp = previousRow[i] and p[i] == s[letter]
                actualRow.append(temp)
            previousRow = actualRow
        return previousRow[len(p)]
