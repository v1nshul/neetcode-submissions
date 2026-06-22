class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)
        l = 0
        r  = l + w
        co = {}
        for i in s1:
            co[i] = 1 + co.get(i,0)
        while l < len(s2):
            sub = s2[l:r]
            sc = {}
            for i in sub:
                sc[i] = 1 + sc.get(i,0)
            if co == sc:
                return True
            l += 1
            r += 1
            if r > len(s2):
                r = len(s2)
            if r - l < w:
                return False
