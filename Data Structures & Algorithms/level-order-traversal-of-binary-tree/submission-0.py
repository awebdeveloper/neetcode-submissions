# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]
        result  = []

        if not root:
            return []

        while stack:
            top, level = stack.pop()

            if level == len(result):
                result.append([])

            result[level].append(top.val)
            
            if top.right:
                stack.append((top.right, level + 1))

            if top.left:
                stack.append((top.left, level + 1))

        return result

