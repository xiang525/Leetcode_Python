class Solution:
    def twoSum(self, lst, target):
        for i in range(len(lst)):
            j = target - lst[i]
            for ii in range(len(lst)-1, i, -1):
                if lst[ii]<j:
                    break
                if lst[ii] == j:
                    return [i+1, ii+1]
        return [-1,-1]
        # for i in lst:
        #   if target - i in lst:
        #       return [lst.index(i)+1, lst.index(target-i)+1]
        # return [-1, -1]

s = Solution()
print s.twoSum([2,2,11,15], 26)