# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not q or not p  or (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack  = [root]

        while stack:
            top = stack.pop()

            if not top:
                continue

            if top.val == subRoot.val:
                result = self.isSameTree(top, subRoot)

                if result:
                    return True

            
            stack.append(top.left)
            stack.append(top.right)

        return False










            

