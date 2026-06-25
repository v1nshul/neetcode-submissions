# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next
        
        s2 = s.next
        p = s.next = None
        while s2:
            t = s2.next
            s2.next = p
            p = s2
            s2 = t
        
        f1, s2 = head,p
        while s2:
            t1,t2 = f1.next,s2.next
            f1.next = s2
            s2.next = t1
            f1,s2 = t1,t2
        