class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        s = 0
        l, r = 1, len(nums) - 1

        res = []

        while s < len(nums) and nums[s] <= 0 and nums[r] >= 0:
            while l < r: 
                sums = nums[s] + nums[l] + nums[r]
                if sums == 0: 
                    res.append([nums[s], nums[l], nums[r]])
                    currl, currr = nums[l], nums[r]

                    while l < r and currl == nums[l]:
                        l += 1
                    while l < r and currr == nums[r]:
                        r -= 1

                elif sums < 0: 
                    l += 1
                else: 
                    r -= 1

            curr_s = nums[s]
            while s < len(nums) and curr_s == nums[s]:
                s += 1
            
            l = s + 1
            r = len(nums) - 1

        return res

            

