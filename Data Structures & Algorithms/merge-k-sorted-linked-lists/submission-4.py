# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pendingList = lists

        if not pendingList:
            return None

        while len(pendingList) > 1: 
            tempMerges = []
            for i in range(0, len(pendingList), 2):
                l1 = pendingList[i]
                l2 = pendingList[i+1] if i+1 < len(pendingList) else None
                tempMerges.append(self.mergeList(l1,l2))

            pendingList = tempMerges

        return pendingList[0]




    def mergeList(self, l1:Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1 and not l2:
            return None

        dummy = ListNode(0)
        root = dummy

        while l1 or l2:
            # no more in l1 append l2 and exit
            if not l1:
                root.next = l2
                break
            
            # no more in l2 append l1 and exit
            if not l2:
                root.next = l1
                break


            # append the smaller node
            if l1.val < l2.val:
                root.next = l1
                l1= l1.next
            else:
                root.next = l2
                l2= l2.next
    
            # increment root
            root = root.next
            root.next = None # saftey hatch

        return dummy.next



             