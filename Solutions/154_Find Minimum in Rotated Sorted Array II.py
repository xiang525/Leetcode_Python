class Solution:
    # @param num, a list of integer
    # @return an integer

    def findMin(self, num):
        i = 0
        length = len(num)
        m = num[0]
        while(i < length-1):
            if num[i + 1] <= num[i]:
                if num[i+1]<m:
                    m = num[i+1]
                i += 1
            else:
                i += 1
        return m
