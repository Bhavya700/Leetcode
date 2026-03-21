# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head
        n = 1
        a = head
        b = head
        while a and a.next:
            a=a.next
            n+=1
        if k>=n:
            k=k%n
        if k==0:
            return head
        for i in range(n-k-1):
            b=b.next

        tmp = b.next
        b.next = None
        a.next = head
        return tmp


