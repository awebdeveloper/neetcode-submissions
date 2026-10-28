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
        queue = [(root,depth)]
        i = 0

        while i < len(queue):
            node, prevLevel = queue[i]
            i += 1

            if node:
                level = prevLevel + 1
                depth = max(depth, level);
                queue.append((node.left, level))
                queue.append((node.right, level))

        return depth



        