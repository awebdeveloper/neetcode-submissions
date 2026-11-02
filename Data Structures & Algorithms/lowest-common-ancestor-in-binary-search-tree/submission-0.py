# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parentsHash = {}
        stack = [(root, [])] # (node, parents)

        # get all parents of a element
        while (p not in parentsHash or q not in parentsHash) and stack:
            node, parents = stack.pop()
            parents = [node, *parents]

            if node == p or node == q:
                parentsHash[node] = parents

            if node.left:
                stack.append((node.left, parents))

            if node.right:
                stack.append((node.right, parents))

        print(parentsHash)
        print("p",p, "q",q)
        # find parent  
        if p in parentsHash and q in parentsHash:      
            seen = set(parentsHash[p])
            for x in parentsHash[q]:   
                if x in seen: 
                    return x

        return root

        
        
