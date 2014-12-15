class Solution:
    # @param num, a list of integer
    # @return an integer

    def findPeakElement(self, num):
        pre_num = [num[i] for i in range(1, len(num))] + [float('-inf')]
        suf_num = [float('-inf')] + [num[i] for i in range(len(num) - 1)]

        sub_num_1 = [n - p for n, p in zip(num, pre_num)]
        sub_num_2 = [n - s for n, s in zip(num, suf_num)]
        for i in range(len(num)):
            if sub_num_1[i] > 0 and sub_num_2[i] > 0:
                return i
        return 0
