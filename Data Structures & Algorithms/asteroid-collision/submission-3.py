class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # sort asteroids based on position. add asteroids to stack. if stack[-1] has a different sign than the current asteroid, process it 
        stack = []

        for a in asteroids: 

            while stack and (stack[-1] > 0 and a < 0): 
                if abs(stack[-1]) < abs(a): 
                    stack.pop()
                elif abs(stack[-1]) == abs(a):
                    stack.pop()
                    a = 0
                    break
                else: 
                    a = 0
                    break 
            
            if a != 0: 
                stack.append(a)
        
        return stack 