# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:    
            if fast.next.next==None:
                fast=slow.next.next
                slow.next=fast
                return head
            else: 
                fast=fast.next.next
            if fast.next==None:
                fast=slow.next.next
                slow.next=fast
                return head
            
            slow=slow.next

         

