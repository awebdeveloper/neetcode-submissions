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
        
        depth = 1
        queue = [(root,depth)]
        i = 0

        while i < len(queue):
            node, prevLevel = queue[i]
            i += 1

            if node and node.left:
                level = prevLevel + 1
                depth = max(depth, level);
                queue.append((node.left, level))

            if node and node.right:
                level = prevLevel + 1
                depth = max(depth, level);
                queue.append((node.right, level))

        return depth



        