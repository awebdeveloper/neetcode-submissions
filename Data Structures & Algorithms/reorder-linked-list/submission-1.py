# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid length
        fast = slow = head
        midCount = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            midCount += 1

        even = (fast == None)


        # handle single node
        nodeLen = 1
        if head.next:
            nodeLen = midCount * 2 + (0 if even else 1)
        

        if nodeLen < 3:
            return None

        # get mid
        mid = slow
        if not even:
            mid = mid.next


        #reverse the mid to get n-1, n-2
        prev = None
        while mid: # decide head or head.next
            next = mid.next
            mid.next = prev 
            prev = mid
            mid = next
        reversedMid = prev

        res = start = ListNode(0)
        headNext = None
        midNext = None

        for i in range(midCount):
            headNext = head.next
            midNext = reversedMid.next

            
            start.next = head
            start.next.next = reversedMid
            start = start.next.next # move start
           

            head = headNext
            reversedMid = midNext


        if not even and headNext:
            start.next = headNext
            start.next.next = None # break the chain

        loop = res
        while loop:
            print (loop.val)
            loop = loop.next

