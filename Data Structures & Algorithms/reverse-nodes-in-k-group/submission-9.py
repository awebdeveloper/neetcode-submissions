# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        root = None
        joinNode = None
        prevJoinNode = None
        curr = None
        count = 0

        if k == 1:
            return node

        while node:
            next = node.next # 2->3...., 3->4...., 4->5..., 5->6....
            node.next = prev # None, 1->none, 2->1->none, none
            prev = node # 1->none, 2->1->none, 3->2->1->none, 4->none
            count += 1

            if count % k == 1:
                joinNode = node #1, 4

            if count % k == 0:
                prev = None

                if not prevJoinNode:
                    root = node
                elif joinNode:
                    prevJoinNode.next = node
                
                prevJoinNode = joinNode

            
            node = next

        
        if count % k != 0:
            node = prev
            prev = None

            while node:
                next = node.next # 5->none, none
                node.next = prev  # 4->none, 5->4->none
                prev = node # 4->none, 5->4->none
                node = next # 5->none, none
            
            if prevJoinNode:
                prevJoinNode.next = prev
            
            print(prev)

            if not root:
                root = node

        return root


    

            
        


            




        
        


