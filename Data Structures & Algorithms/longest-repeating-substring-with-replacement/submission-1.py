class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        cs = set(s)
        for c in cs:
            ct = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    ct += 1
                while (r-l+1) - ct > k:
                    if s[l] == c:
                        ct -= 1
                    l += 1
                res = max(res, r-l +1)
        return res