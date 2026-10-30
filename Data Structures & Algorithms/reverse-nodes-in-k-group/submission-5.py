# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        heads = []
        tails = []
        mainHead = head
        node = head
        prev = None

        length = 0

        if k == 1:
            return mainHead
            
        # reverse in groups
        while node:
            next = node.next
            node.next = prev
            prev = node
            length += 1

            # capture tails
            if length % k == 1:
                tails.append(node)

            # break the list on reaching k
            if length % k == 0:
                heads.append(node)
                prev = None
            

            node = next

        # reverse the last one if its not exactly k
        if length % k != 0:
            node = prev
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            heads.append(prev)
            

        for i in range(1, len(heads)):
            tails[i-1].next = heads[i]


        return heads[0]





