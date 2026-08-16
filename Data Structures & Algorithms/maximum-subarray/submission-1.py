class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        s = ret

        for i in range(1, len(nums)):
            if (s < 0):
                s = 0
            ret = max(ret, nums[i] + s)
            s += nums[i]

        
        return ret


            

            
        