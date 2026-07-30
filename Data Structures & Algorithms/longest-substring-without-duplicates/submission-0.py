class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        subs = 1

        l = 0
        r = l + 1

        while l < len(s) and r < len(s):
            curs = 1
            set1 = set()
            if s[l] not in set1:
                set1.add(s[l])
            while r < len(s) and s[r] != s[l] and s[r] not in set1:
                curs += 1
                set1.add(s[r])
                r += 1
            subs = max(subs, curs)
            l += 1
            r = l +1

        return subs
            
