class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        nums.append(0)
        nums.insert(0, 0)

        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        
        return max(nums[-1], nums[-2])
