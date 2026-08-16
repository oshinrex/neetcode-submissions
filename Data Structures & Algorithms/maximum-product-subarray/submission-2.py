class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        curMax = nums[0]
        curMin = nums[0]
    
        for i in range(1, len(nums)):
            temp = max(nums[i], curMax*nums[i], curMin*nums[i])
            curMin = min(nums[i], curMax*nums[i], curMin*nums[i])
            curMax = temp
            max_prod = max(max_prod, curMax, curMin)
            print(curMax)
            print(curMin)
            print(max_prod)

        return max_prod