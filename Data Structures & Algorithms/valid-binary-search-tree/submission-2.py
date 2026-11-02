# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float("-infinity"), float("infinity"))]

        while stack:
            top, left, right = stack.pop()

            if not top:
                continue

            if not (left < top.val < right):
                return False
                
            stack.append((top.left, left, top.val))
            stack.append((top.right, top.val, right))
        return True