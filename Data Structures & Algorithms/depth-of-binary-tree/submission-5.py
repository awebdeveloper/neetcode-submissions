# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMaxDepth(self, root: Optional[TreeNode], level: int) -> int:
        newDepth = 0
        if root:
            newLevel = level + 1
            maxLeft = self.getMaxDepth(root.left, newLevel)
            maxRight = self.getMaxDepth(root.right, newLevel)

            newDepth = max(maxLeft, maxRight)

        return max(newDepth, level)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root, 0)
        