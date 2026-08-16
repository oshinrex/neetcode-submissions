class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        n1 = nums[0]
        c1 = 0
        n2 = nums[1]
        c2 = 0

        for n in nums: 
            if n == n1: 
                c1 += 1
            elif n == n2: 
                c2 += 1
            elif c1 == 0: 
                n1 = n
                c1 = 1
            elif c2 == 0:
                n2 = n
                c2 = 1
            else: 
                c1 -= 1
                c2 -= 1
        
        r1 = 0
        r2 = 0

        for n in nums: 
            if n == n1: 
                r1 += 1
            if n == n2: 
                r2 += 1
        
        res = []
        if r1 > len(nums) // 3: 
            res.append(n1)
        
        if n1 != n2 and r2 > len(nums) // 3: 
            res.append(n2)
        
        return res
