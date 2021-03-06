class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.ret:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i + 1, valuelist + [candidates[i]])

    def combinationSum2(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret
