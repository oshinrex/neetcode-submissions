class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        cand = nums[0]

        for n in nums:
            if count == 0:
                cand = n
            if cand == n:
                count += 1
            else:
                count -= 1
        
        return cand
