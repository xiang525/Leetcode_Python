# wiki: Roman Number: http://en.wikipedia.org/wiki/Roman_numerals
class Solution:
    # @return a string

    def intToRoman(self, num):
        result = ""
        transTable = {
            1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        for trans in sorted(transTable.keys())[::-1]:
            while num != 0 and num >= trans:
                num -= trans
                result += transTable[trans]
            if num == 0:
                break

        simplifyTable = {"DCCCC": "CM", "CCCC": "CD", "LXXXX":
                         "XC", "XXXX": "XL", "VIIII": "IX", "IIII": "IV"}
        simplifyContent = ["DCCCC", "CCCC", "LXXXX", "XXXX", "VIIII", "IIII"]
        for item in simplifyContent:
            if item in result:
                result = result.replace(item, simplifyTable[item])

        return result
