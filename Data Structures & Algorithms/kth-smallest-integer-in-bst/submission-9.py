# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, False)]
        top = None
        count = 0


        while stack and k > count:
            top, processsed = stack.pop()

            if processsed == True:
                count += 1
                continue


            if top.right:
                stack.append((top.right, False))

            stack.append((top, True))
                
            if top.left:
                stack.append((top.left, False))

        if top:
            return top.val


    
