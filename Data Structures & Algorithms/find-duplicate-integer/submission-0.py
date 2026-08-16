class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = 0
        s = 0

        # find first collision 
        while True:
            f = nums[nums[f]]
            s = nums[s]
            if f == s:
                break
        
        new_s = 0
        # find second collision 
        while True:
            new_s = nums[new_s]
            s = nums[s]
            if new_s == s:
                break
        
        return s