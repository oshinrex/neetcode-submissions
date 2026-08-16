class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            max_jump = 0
            for i in range(l, r + 1):
                max_jump = max(nums[i] + i, max_jump)
            l = r + 1
            r = max_jump
            res += 1
        
        return res