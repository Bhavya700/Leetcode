# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False

        i = head
        j = head
        while j.next!= None and j.next.next!= None:
            i=i.next
            j=j.next.next
            if i is j:
                return True

        return False