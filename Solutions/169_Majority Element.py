class Solution:
    # @param num, a list of integers
    # @return an integer

    def majorityElement(self, num):
        count = {}
        for i in num:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        return max(count, key=count.get)
