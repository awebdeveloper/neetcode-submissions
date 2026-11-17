"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def visit(original: Optional['Node'])  -> Optional['Node']:
            if not original:
                return None

            if original in visited:
                return visited[original]

            newCopy = Node(original.val)
            visited[original] = newCopy
            for neighbour in original.neighbors:
                newCopy.neighbors.append(visit(neighbour))
            
            return newCopy

        return visit(node)




        