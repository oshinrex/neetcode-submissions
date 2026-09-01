class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if number, append to stack 
        # if symbol, pop last 2 element and add to the stack 
        # return the final number in the stack 

        stack = []
        symbols = {"+", "-", "/", "*"}

        for t in tokens: 
            n1, n2 = 0, 0
            if t in symbols: 
                n2 = stack.pop()
                n1 = stack.pop()
            if t == "+": 
                stack.append(n1 + n2) 
            elif t == "-":
                stack.append(n1 - n2) 
            elif t == "*": 
                stack.append(n1 * n2) 
            elif t == "/": 
                stack.append(int(n1 / n2))
            else: 
                stack.append(int(t))
        
        return stack[0]