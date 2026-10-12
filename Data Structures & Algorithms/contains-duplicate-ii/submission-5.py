class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: 
            return False
            
        l = 0
        s = set()

        for i in range(len(nums)):
            if nums[i] in s: 
                return True 
            else:
                if len(s) == k:
                    s.discard(nums[i - k])
                s.add(nums[i])
        
        return False
            
            
