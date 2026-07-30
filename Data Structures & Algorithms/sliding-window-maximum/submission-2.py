class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            n = max(nums)
            return [n]
        res = []
        l = 0
        r = l + k

        while r < len(nums):
            curm = max(nums[l:r])
            res.append(curm)
            l += 1
            r += 1
            if r == len(nums):
                res.append(max(nums[l:r]))
                break
            
        return res