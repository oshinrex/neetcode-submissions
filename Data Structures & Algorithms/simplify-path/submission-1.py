class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        res = []
        i = 0
        
        while i < len(stack): 
            if not stack[i]: 
                i += 1
            elif stack[i] == ".." and res: 
                res.pop()
                i += 1
            elif stack[i] == ".." or stack[i] == ".":
                i += 1
            else: 
                res.append(stack[i])
                i += 1

        return "/" + "/".join(res)
