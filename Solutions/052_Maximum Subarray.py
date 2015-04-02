class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxSubArray(self, A):
        length = len(A)
        max_dp = [0] * (length)
        if A:
            max_dp[0] = A[0]
        for i in range(1, length):
            max_dp[i] = max(max_dp[i - 1] + A[i], A[i])
        return max(max_dp)
