class Solution:
    # @param A, a list of integers
    # @return a boolean

    # def canJump(self, A):
    #     reachable = 0
    #     while reachable < len(A) - 1 and A[reachable] != 0:
    #         reachable = reachable + A[reachable]
    #     if reachable == len(A) - 1:
    #         return True
    #     else:
    #         return False

    def canJump(self, A):
        reachable = 0
        for i in range(len(A)):
            if i > reachable:
                return False
            reachable = max(reachable, i + A[i])
        return True
