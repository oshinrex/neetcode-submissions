class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # in order for asteroids to collide, prev asteroid must be moving + and curr asteroid moving - 
        stack = []

        for a in asteroids: 
            while a < 0 and stack and stack[-1] > 0: 
                if stack[-1] < abs(a): 
                    stack.pop()
                elif stack[-1] == abs(a): 
                    stack.pop()
                    a = 0 
                    break
                else: 
                    a = 0 
                    break
            if a != 0: 
                stack.append(a)
        
        return stack