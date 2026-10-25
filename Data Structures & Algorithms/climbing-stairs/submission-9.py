class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n 

        one, two = 1, 2

        for i in range(2, n): 
            temp = one 
            one = two 
            two = temp + two 
        
        return two 
