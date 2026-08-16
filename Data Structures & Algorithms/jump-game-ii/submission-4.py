class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0 
        l = 0 
        r = 0

        jumps = 0

        while r < len(nums) - 1:
            for i in range(l, r+1):
                furthest = max(furthest, i + nums[i])
            l = r
            r = furthest
            jumps += 1
        
        return jumps
        