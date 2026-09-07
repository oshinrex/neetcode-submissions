class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        toAdd = ""

        for i in range(len(s)):
            if s[i] == "[":
                stack.append(toAdd)
                toAdd = ""
            elif s[i] == "]":
                word = toAdd

                if not word:
                    word = stack.pop()
                
                phrase = word
                
                while stack and stack[-1].isalpha(): 
                    phrase = stack.pop() + phrase

                num = int(stack.pop())
                phrase = phrase * num

                while stack and stack[-1].isalpha(): 
                    phrase = stack.pop() + phrase
                stack.append(phrase)
                toAdd = ""
            elif s[i].isalpha() and (not toAdd or toAdd.isalpha()):
                toAdd += s[i]
            elif s[i].isdigit() and (not toAdd or toAdd.isdigit()):
                toAdd += s[i]
            else: 
                stack.append(toAdd)
                toAdd = s[i]
        return "".join(stack) + toAdd