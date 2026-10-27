# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return node
        
        stack = [node]

        while stack:
            top = stack.pop()
            top.left, top.right = top.right, top.left

            if top.left:
                stack.append(top.left)

            if top.right:
                stack.append(top.right)

        return node;

            

            


            


            