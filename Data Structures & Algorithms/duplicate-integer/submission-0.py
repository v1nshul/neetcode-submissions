class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i,0)
        for i in d.values():
            if i != 1:
                return True
        return False