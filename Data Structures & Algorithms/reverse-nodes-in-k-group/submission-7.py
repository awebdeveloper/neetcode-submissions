# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        mainHead = head
        node = head
        prev = None
        prevTail = None
        tail = None

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
                tail = node

            # break the list on reaching k
            if length % k == 0:
                if prevTail:
                    prevTail.next = node
                else:
                    mainHead = node
                prev = None
                prevTail = tail
                tail = None
            

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

            if prevTail:
                prevTail.next = prev
            else:
                mainHead = prev

        return mainHead





