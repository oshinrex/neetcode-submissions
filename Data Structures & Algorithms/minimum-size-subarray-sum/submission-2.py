class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        min_len = len(nums) + 1

        for r in range(len(nums) + 1):
            while curr_sum >= target:
                print(curr_sum) 
                min_len = min(r - l, min_len)
                curr_sum -= nums[l]
                l += 1
            if r != len(nums):
                curr_sum += nums[r]
        
        return 0 if min_len == len(nums) + 1 else min_len