"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = Node(0)
        copyHead = copy
        hash = {None: None}
        original = head

        # empty return
        if not original:
            return None

        # create a copy and record the random
        i = 0
        while original:
            newNode = Node(original.val)
            hash[original] = newNode

            copy.next = newNode
            copy = copy.next
            original = original.next
            i +=1

        # copy random
        original = head
        copy = copyHead.next
        while original:
            copy.random = hash[original.random]
            original = original.next
            copy = copy.next

        return copyHead.next



