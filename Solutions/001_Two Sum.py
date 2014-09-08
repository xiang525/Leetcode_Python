class Solution:
    # @return a tuple, (index1, index2)

    def twoSum(self, num, target):
        for i in sorted(num, reverse=True):
            if target - i in num:
                return (num.index(i) + 1, num.index(target - i) + 1)
        return (-1, -1)
