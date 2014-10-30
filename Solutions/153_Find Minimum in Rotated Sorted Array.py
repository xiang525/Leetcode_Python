class Solution:
    # @param num, a list of integer
    # @return an integer

    def findMin(self, num):
        i = 0
        length = len(num)
        while(i < length-1):
            if num[i + 1] < num[i]:
                return num[i + 1]
            else:
                i += 1
        return num[0]
