# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        dummy = ListNode(0, head)
        r = head
        l = dummy
        while r and n>0:
            r = r.next
            n-=1

        while r is not None:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next