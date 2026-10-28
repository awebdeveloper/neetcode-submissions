# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root)[1]

    def getMaxDepth(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if not root:
            return (0, 0)

        leftDepth, leftDiameter = self.getMaxDepth(root.left)
        rightDepth, rightDiameter = self.getMaxDepth(root.right)

        depth = max(leftDepth, rightDepth) + 1
        diameter = max(leftDepth + rightDepth, leftDiameter, rightDiameter)

        return (depth, diameter)


    






        