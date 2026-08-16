class Solution:
    def climbStairs(self, n: int) -> int:
        # n: number of steps to reach the top of a staircase
        # can climb with either 1 or 2 steps at a time 
        # return num of distince ways to climb to the top of the staircase
        
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two 
            two = temp

        return one 

