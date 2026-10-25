# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        node, prev = head, None
        while node:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode

        return prev

'''
    x->y->z

    node = x->y->z->a
    nextNode = y->z->a
    node = x->None
    prev = x->none
    node = y->z->a


    node = y->z->a
    nextNode = z->a
    node = y->x->none
    prev = y->z->a
    node = z->a

    node = z->a
    nextNode = a
    node = z->y->x->none
    prev = z->a
    node = a

    node = a
    nextNode = none
    node = a->z->y->x->none
    prev = a
    node = none
'''
