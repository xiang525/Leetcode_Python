class Solution:
    # @return a string

    def convertToTitle(self, num):
        alpha = [chr(i) for i in range(65, 91)]
        res = []
        while num > 0:
            t = num % 26
            print t
            res.append(alpha[t - 1])
            num = (num / 26)
            if t == 0:
                num -= 1
        return ''.join(res[::-1])
