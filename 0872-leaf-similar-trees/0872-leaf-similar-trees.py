# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def fun(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from fun(node.right)
                yield from fun(node.left)
        return list(fun(root1)) == list(fun(root2))