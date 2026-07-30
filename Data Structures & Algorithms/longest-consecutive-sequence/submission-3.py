class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_s = 0
        s = set(nums)

        for i in s:
            if i -1 not in s:
                cur_s = 1
                cur = i
                while cur + 1 in s:
                    cur_s += 1
                    cur += 1 
                    
                max_s = max(max_s, cur_s)

        return max_s