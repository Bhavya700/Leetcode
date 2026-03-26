# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        l = head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        r = slow
        temp = r.next
        r.next = None
        r = temp
        l = self.sortList(l)
        r = self.sortList(r)

        return self.merge(l, r)
    
    def merge(self, l1, l2):
        tail = dummy = ListNode()
        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail=tail.next
        
        if l1:
            tail.next=l1
        if l2:
            tail.next=l2
        
        return dummy.next