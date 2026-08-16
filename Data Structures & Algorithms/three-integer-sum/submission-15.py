class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0

        while i < len(nums) - 2:  
            if nums[i] > 0: 
                return res 
            
            j, k = i + 1, len(nums) - 1

            while j < k: 
                if nums[k] + nums[j] == -nums[i]: 
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < len(nums) and nums[j - 1] == nums[j]: 
                        j += 1
                elif nums[k] + nums[j] < -nums[i]: 
                    j += 1
                else: 
                    k -= 1
            
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]: 
                i += 1
        
        return res
            