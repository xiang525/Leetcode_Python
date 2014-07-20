class Solution:
    # @return an integer

    def reverse(self, x):
        tmp = str(x)
        tmp = "-" + tmp[:0:-1] if tmp.startswith("-") else tmp[::-1]
        return int(tmp)
