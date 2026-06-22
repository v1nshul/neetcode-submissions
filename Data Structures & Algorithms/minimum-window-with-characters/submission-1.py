class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        ct = {}
        for c in t:
            ct[c] = 1 + ct.get(c,0)
        res, reslen= [-1,-1], float("infinity")
        for i in range(len(s)):
            cs = {}
            for j in range(i,len(s)):
                cs[s[j]] = 1 + cs.get(s[j],0)
                flag = True
                for c in ct:
                    if ct[c] > cs.get(c,0):
                        flag = False
                        break
                if flag and (j-i+1) < reslen :
                    reslen = j-i+1
                    res = [i,j]
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""           
                    
