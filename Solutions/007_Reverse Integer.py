class Solution:
    # @return an integer

    def reverse(self, x):
        tmp = str(x)
        tmp = "-" + tmp[:0:-1] if tmp.startswith("-") else tmp[::-1]
        if int(tmp) > 2 ** 31 - 1 or int(tmp) < -2 ** 31 + 1:
            return 0
        else:
            return int(tmp)
