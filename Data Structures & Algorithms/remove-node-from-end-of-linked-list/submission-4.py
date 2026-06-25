# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c= head
        ar = []
        while c:
            ar.append(c)
            c = c.next
        
        if len(ar) - n == 0:
            return head.next
        
        ar[len(ar) - n-1].next = ar[len(ar)-n].next
        return head



