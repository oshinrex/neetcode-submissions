class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: 
            return n
            
        dp = [0] * (n)
        one, two = 1, 2
        for i in range(2, n): 
            temp = one
            one = two 
            two = two + temp
        
        return two
            

