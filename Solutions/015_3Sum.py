class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]

    def threeSum(self, num):
        """ TLE version """
        # result_list = []
        # length = len(num)
        # if length < 3:
        #     return []
        # origin = list(num)
        # for i in range(length):
        #     for j in range(i + 1, length):
        #         m = num[i]
        #         n = num[j]
        #         seek = 0 - m - n
        #         num.pop(j)
        #         num.pop(i)
        #         if seek in num:
        #             result = sorted([m, n, seek])
        #             if result not in result_list:
        #                 result_list.append(result)
        #         num = list(origin)
        # return result_list

        num, result, i = sorted(num), [], 0
        while i < len(num) - 2:
            j, k = i + 1, len(num) - 1
            while j < k:
                if num[i] + num[j] + num[k] < 0:
                    j += 1
                elif num[i] + num[j] + num[k] > 0:
                    k -= 1
                else:
                    result.append([num[i], num[j], num[k]])
                    j, k = j + 1, k - 1
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    while j < k and num[k] == num[k + 1]:
                        k -= 1
            i += 1
            while i < len(num) - 2 and num[i] == num[i - 1]:
                i += 1
        return result
