class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def helper(num): 
            if len(num) == 0:
                return 0
            dp = [0] * len(num)
            dp[0] = num[0]
            max_ret = dp[0]

            for i in range(1, len(num)):
                max_num = 0
                for j in range(i - 1):
                    max_num = max(max_num, dp[j])
                dp[i] = max_num + num[i]
                max_ret = max(max_ret, dp[i])
            return max_ret
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
