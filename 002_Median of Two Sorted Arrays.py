# Note: Done
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        temp = sorted(A + B)
        if len(temp) % 2 == 0:
            return (temp[len(temp)/2] + temp[len(temp)/2 - 1]) / 2.0
        else:
            return temp[len(temp)/2]

# Problem: There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).

