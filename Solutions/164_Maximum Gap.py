class Solution:
    # @param num, a list of integer
    # @return an integer

    def maximumGap(self, num):
        num = sorted(num)
        if len(num) in [0, 1]:
            return 0
        new_num = [num[0]] + [num[i] for i in range(len(num) - 1)]
        sub_num = [a-b for a, b in zip(num, new_num)]
        return max(sub_num)