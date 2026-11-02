# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float("-infinity"))]
        count  = 0

        while stack: # [1]* [2, 1] [2]* [3,4] [] 
            top, largestParent = stack.pop()
            if top.val >= largestParent:
                count += 1
                largestParent = top.val

            if top.left:
                stack.append((top.left, largestParent))

            if top.right:
                stack.append((top.right, largestParent))


        
        return count

            
   
