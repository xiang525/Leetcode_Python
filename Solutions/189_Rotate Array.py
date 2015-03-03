class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        return nums[n-k:n]+nums[:n-k]

s = Solution()
s.rotate([1,2], 1)