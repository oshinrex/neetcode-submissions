class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr = ""

        for c in s: 
            if c.isdigit(): 
                num = num * 10 + int(c)
            elif c == "[": 
                stack.append((curr, num))
                num = 0
                curr = ""
            elif c == "]":
                prev, count = stack.pop()
                curr = prev + (curr * count)

            else: 
                print(curr)
                print(c)
                curr += c 
        
        return curr