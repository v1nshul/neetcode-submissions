class Solution:

    def encode(self, strs: List[str]) -> str:
        
        enc = ''
        for s in strs:
            enc += str(len(s)) +'#' + s
        return enc
         
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j = j+1
            l = int(s[i:j])
            i = j+1
            j = i + l
            res.append(s[i:j])
            i = j

        return res
        
            
