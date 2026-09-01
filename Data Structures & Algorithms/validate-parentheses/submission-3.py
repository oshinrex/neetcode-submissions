class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'}':'{', ']':'[', ')':'('}

        for i in range(len(s)):
            if s[i] in d: 
                if not stack or stack[-1] != d[s[i]]:
                    return False 
                stack.pop()
            else: 
                stack.append(s[i])
        
        return True if not stack else False