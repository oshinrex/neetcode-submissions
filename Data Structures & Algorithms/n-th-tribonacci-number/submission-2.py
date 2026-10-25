class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: 
            return n 
        
        if n == 2: 
            return 1 
        
        zero, one, two = 0, 1, 1

        for i in range(2, n):
            temp = two 
            two = zero + one + two 
            zero = one 
            one = temp 
        
        return two

        