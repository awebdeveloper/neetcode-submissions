# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        array = [(p,q)]
        i = 0;

        while i < len(array):
            left, right = array[i]
            i += 1

            # both at none skip
            if not left and not right:
                continue

            # one is none mismatch
            if not left or not right:
                return False

            # value mismatch
            if left.val != right.val:
                return False

            array.append((left.left, right.left))
            array.append((left.right, right.right))

        return True

            
        