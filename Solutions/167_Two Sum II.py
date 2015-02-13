class Solution:
	def twoSum(self, lst, target):
		for i in lst:
			if target - i in lst:
				return [lst.index(i)+1, lst.index(target-i)+1]
		return [-1, -1]

s = Solution()
s.twoSum([2,7,11,15], 9)