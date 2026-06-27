class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = {}

        for i in nums:
            m[i] = 1 + m.get(i,0)
        
        for i,j in m.items():
            if j > 1:
                return i
            