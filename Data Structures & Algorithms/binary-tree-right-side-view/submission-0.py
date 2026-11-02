# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 

        result = []
        stack = [(root, 0)]
        while stack:
            top, level = stack.pop()

            if len(result) == level:
                result.append(top.val)


            if top.left:
                stack.append((top.left, level + 1))
            
            if top.right:
                stack.append((top.right, level + 1))

        return result