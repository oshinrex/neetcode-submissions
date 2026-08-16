class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "*+-/"
        
        for t in tokens: 
            if t in operators: 
                snd = stack.pop()
                fst = stack.pop()
                if t == "*": 
                    stack.append(snd * fst)
                elif t == "+": 
                    stack.append(snd + fst)
                elif t == "-": 
                    stack.append(fst - snd)
                else: 
                    stack.append(int(fst/snd))
            else: 
                stack.append(int(t))
            print(stack)

        return stack[0]