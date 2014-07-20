class Solution:
    # @return a float

    def findMedianSortedArrays(self, A, B):
        temp = sorted(A + B)
        if len(temp) % 2 == 0:
            return (temp[len(temp) / 2] + temp[len(temp) / 2 - 1]) / 2.0
        else:
            return temp[len(temp) / 2]
