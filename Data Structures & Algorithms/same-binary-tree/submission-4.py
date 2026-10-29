# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackP = [p]
        stackQ = [q]
        isValid = True

        while isValid and (stackQ or stackP):
            if not stackP or not stackQ:
                isValid = False
                break
            
            topP = stackP.pop()
            topQ = stackQ.pop()

            if not topP and not topQ:
                continue
            
            if not topP or not topQ or topP.val != topQ.val:
                isValid = False
                break

            stackP.append(topP.left)
            stackP.append(topP.right)

            stackQ.append(topQ.left)
            stackQ.append(topQ.right)

        return isValid
            