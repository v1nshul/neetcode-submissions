class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for c in s:
            if c in m:
                if len(stack)>0 and stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
            else: stack.append(c)

        return len(stack)==0
            