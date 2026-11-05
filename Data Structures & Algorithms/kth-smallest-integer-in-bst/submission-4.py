# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = 0
        count = 0

        stack = [(root, False)]
        valList = []
        count = 0

        while stack and count < k:
            node, processed = stack.pop()

            if not node:
                continue

            if processed:
                count += 1
                valList.append(node.val)
                continue


            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))

        return valList[-1]

       
        


            
        