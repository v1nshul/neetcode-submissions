class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        max_s = 1
        cur = 0
        s = set(nums)
        for i in s:
            cur_s = 1
            cur = i
            while cur + 1 in s:
                cur_s += 1
                max_s = max(max_s, cur_s)
                cur = cur+1

        return max_s