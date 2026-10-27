# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = [root]
        counter = 0
        
        while queue and counter < len(queue):
            node = queue[counter]
            counter += 1

            if node and node.left:
                queue.append(node.left)

            if node and node.right:
                queue.append(node.right)

        for node in queue:
            node.left, node.right = node.right, node.left

        return root;

           