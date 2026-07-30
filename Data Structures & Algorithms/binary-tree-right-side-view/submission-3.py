# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque([root])

        while q:
            r = None
            ql = len(q)
            for i in range(ql):
                n = q.popleft()
                if n:
                    r = n
                    q.append(n.left)
                    q.append(n.right)
            if r:
                res.append(r.val)
        return res
