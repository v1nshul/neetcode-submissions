# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        c = head
        s = set()

        while c:
            if c in s:
                return True
            s.add(c)
            c = c.next
        return False