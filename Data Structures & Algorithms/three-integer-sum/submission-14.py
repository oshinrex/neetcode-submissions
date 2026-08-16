class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        s, l, r = 0, 1, len(nums) - 1

        res = []

        while s < len(nums) and nums[s] <= 0 and nums[r] >= 0:
            while l < r: 
                sums = nums[s] + nums[l] + nums[r]
                if sums == 0: 
                    res.append([nums[s], nums[l], nums[r]])
                    curl, curr = nums[l], nums[r]
                    while l < r and curr == nums[r]: 
                        r -= 1
                    while l < r and curl == nums[l]: 
                        l += 1
                elif sums < 0: 
                    l += 1
                else: 
                    r -= 1 
            curs = nums[s]
            while s < len(nums) and curs == nums[s]: 
                s += 1
            l, r = s + 1, len(nums) - 1
        
        return res
            


            

