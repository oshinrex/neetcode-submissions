class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 represents house 1 max amt robbed 
        # rob2 represents house 2 max amt robbed
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            temp = rob2
            rob2 = max(rob1 + nums[i], rob2)
            rob1 = temp 
        
        return rob2
