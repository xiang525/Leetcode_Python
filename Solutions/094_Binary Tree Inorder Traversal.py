
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def iterative_inorder(self, root, tree_list):
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                tree_list.append(root.val)
                root = root.right
        return tree_list

    def recursive_inorder(self, root, tree_list):
        if root:
            self.recursive_inorder(root.left, tree_list)
            tree_list.append(root.val)
            self.recursive_inorder(root.right, tree_list)

    def inorderTraversal(self, root):
        tree_list = []
        # the iterative way
        self.iterative_inorder(root, tree_list)
        # the recursive way
        # self.recursive_inorder(root, tree_list)
        return tree_list
