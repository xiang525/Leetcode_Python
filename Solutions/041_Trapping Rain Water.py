class Solution:
    # @param A, a list of integers
    # @return an integer

    def trap(self, A):
        # from right to left
        leftmosthigh = [0 for i in range(len(A))]
        leftmax = 0
        for i in range(len(A)):
            if A[i] > leftmax:
                leftmax = A[i]
            leftmosthigh[i] = leftmax
        # from left to right 
        rightmosthigh = [0 for i in range(len(A))]
        rightmax = 0
        for i in reversed(range(len(A))):
            if A[i] > rightmax:
                rightmax = A[i]
            rightmosthigh[i] = rightmax
        # print rightmosthigh
        total = 0
        for i in range(len(A)):
            if min(rightmosthigh[i], leftmosthigh[i]) > A[i]:
                total += min(rightmosthigh[i], leftmosthigh[i]) - A[i]
        return total
