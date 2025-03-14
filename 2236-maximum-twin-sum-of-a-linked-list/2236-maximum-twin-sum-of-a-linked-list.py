# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        sum=0
        slow=fast=head
        p=None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = p
            p = slow
            slow = nxt
            
        while slow:
            sum=max(sum,slow.val+p.val)
            slow=slow.next
            p=p.next

        return sum