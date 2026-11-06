# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build(self, preorder: List[int], inorder: List[int], iStart: int, iEnd: int, pStart: int, pEnd: int, hash: dict) -> Optional[TreeNode]:      

        if iStart > iEnd or pStart > pEnd:
            return None

        node = TreeNode(preorder[pStart])
        mid = hash[preorder[pStart]]

        leftSize = mid - iStart

        node.left = self.build(
            preorder, 
            inorder, 
            iStart, 
            mid-1, 
            pStart+1, 
            pStart+leftSize,
            hash
        )
        node.right = self.build(
            preorder, 
            inorder, 
            mid+1, 
            iEnd, 
            pStart+leftSize+1, 
            pEnd,
            hash
        )

        return node

    def buildTree(self, preorder: List[int], inorder: List[int])-> Optional[TreeNode]:

        end = len(inorder) - 1
        self.hash = {}

        for i, num in enumerate(inorder):
            self.hash[num] = i
        
        return self.build(preorder, inorder, 0, end, 0, end, self.hash)