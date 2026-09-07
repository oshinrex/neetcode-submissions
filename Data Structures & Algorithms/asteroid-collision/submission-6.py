class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids: 
            if a > 0: 
                stack.append(a)
            else: 
                add = True 
                while stack and stack[-1] > 0: 
                    if -a > stack[-1]: 
                        stack.pop()
                    elif -a == stack[-1]: 
                        stack.pop()
                        add = False
                        break 
                    else: 
                        add = False
                        break

                if add: 
                    stack.append(a)
        
        return stack