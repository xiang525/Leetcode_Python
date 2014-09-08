# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @return a list of tree node

    def generateTrees(self, n):
        return self.generateTreesRecur(1, n)

    def generateTreesRecur(self, low, high):
        result = []
        if low > high:
            result.append(None)
        for i in range(low, high + 1):
            left = self.generateTreesRecur(low, i - 1)
            right = self.generateTreesRecur(i + 1, high)
            for j in left:
                for k in right:
                    current = TreeNode(i)
                    current.left = j
                    current.right = k
                    result.append(current)
        return result
