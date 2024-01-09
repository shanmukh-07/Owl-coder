# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def fun(node):
            l = []
            if node:
                if not node.left and not node.right:
                    l.append(node.val)
                l += fun(node.right)
                l += fun(node.left)
            return l
        return fun(root1) == fun(root2)