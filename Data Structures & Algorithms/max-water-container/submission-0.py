class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0
        
        l,r = 0, len(heights) -1

        while l < r:
            curh = min(heights[l],heights[r])
            cura = curh*(r-l)
            maxa = max(maxa,cura)
            r -= 1
            if r <= l:
                l += 1
                r = len(heights) - 1
        return maxa
        