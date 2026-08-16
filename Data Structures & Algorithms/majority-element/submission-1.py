class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 0

        for n in nums:
            if count == 0: 
                curr = n
                count += 1
            elif curr != n:
                count -= 1
            else:
                count += 1
        
        return curr