class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        prefix = ret

        for i in range(1, len(nums)):
            if (prefix < 0):
                prefix = 0
            prefix += nums[i]
            ret = max(ret, prefix)

        return ret

            
        