# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        sec = s.next
        p = s.next = None
        while sec:
            t = sec.next
            sec.next = p
            p = sec
            sec = t
        
        f,s = head, p
        while s:
            t1,t2 = f.next,s.next
            f.next = s
            s.next =t1
            f,s = t1,t2