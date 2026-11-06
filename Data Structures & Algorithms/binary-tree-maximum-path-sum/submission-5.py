# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.result = float("-infinity")

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            lMax = dfs(node.left)
            rMax = dfs(node.right)

            self.result = max(
                self.result, 
                lMax + rMax + node.val, 
                rMax + node.val, 
                lMax + node.val,
                node.val
            )
            return max(lMax, rMax, 0) + node.val

        dfs(root)
        return self.result

