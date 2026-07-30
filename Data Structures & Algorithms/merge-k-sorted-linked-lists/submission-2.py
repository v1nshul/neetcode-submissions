# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        nodes.sort()
        
        res = ListNode(0)
        c = res
        for n in nodes:
            c.next = ListNode(n)
            c = c.next
        return res.next