# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for _ in range(n):
                fast = fast.next #1


        while fast and fast.next:  #1
            slow = slow.next #1
            fast = fast.next #2


        if slow.next:
            slow.next = slow.next.next

        return dummy.next
        