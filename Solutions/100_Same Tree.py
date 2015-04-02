# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean

    def isSameTree(self, p, q):
        # recursive way
        # if p == None and q is None:
        #     return True
        # elif p is None or q is None or p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # iterative way
        s = []
        s.append(p)
        s.append(q)

        while len(s):
            p = s.pop()
            q = s.pop()

            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            s.append(p.left)
            s.append(q.left)

            s.append(p.right)
            s.append(q.right)
        return True 