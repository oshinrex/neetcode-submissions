class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 0

        for n in nums:
            if count == 0: 
                curr = n
            count += (1 if curr == n else -1)
        
        return curr