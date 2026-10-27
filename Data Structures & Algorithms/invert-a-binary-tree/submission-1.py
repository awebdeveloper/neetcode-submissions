# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        left, right = None, None
        if node and node.left:
            left = self.invertTree(node.left)

        if node and node.right:
            right = self.invertTree(node.right)

        if node: 
            node.left = right
            node.right = left
        return node

        