class Solution:
    def rob(self, nums: List[int]) -> int:
        def solver(i, j):
            dp = [0] * (j - i)
            dp[0] = nums[i]
            
            print(i)
            print(j - 1)
            if i + 1 != j: 
                dp[1] = max(nums[i], nums[i + 1])

            for k in range(i + 2, j):
                dp[k - i] = max(dp[k - 1 - i], nums[k] + dp[k - 2 - i])
            
            return dp[len(dp) - 1]
        
        if len(nums) == 1:
            return nums[0]

        print(solver(1, len(nums)))
        print(solver(0, len(nums) - 1))
        return max(solver(1, len(nums)), solver(0, len(nums) - 1))