# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        stack = [(root, depth)]

        while stack:
            node, prevLevel = stack.pop()

            if node :
                level = prevLevel + 1
                depth = max(depth, level);
                stack.append((node.left, level))
                stack.append((node.right, level))

        return depth
                







