# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        stack: List[Optional[TreeNode]] = [root]
        result = ""

        while (stack):
            node = stack.pop()
            result += "," + (str(node.val) if node else "N")

            if node:
                stack.append(node.right)
                stack.append(node.left)

        return result[1:]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        self.queue = [None if x == "N" else TreeNode(int(x)) for x in data.split(",")]
        self.i = 0
        
        def dfs() -> Optional[TreeNode]:
            node = self.queue[self.i]
            self.i += 1

            if node:
                node.left = dfs()
                node.right = dfs()

            return node


        return dfs()

