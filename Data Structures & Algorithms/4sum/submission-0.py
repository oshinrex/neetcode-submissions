class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []

        while i < len(nums) - 3: 
            j = i + 1
            while j < len(nums) - 2: 
                k, l = j + 1, len(nums) - 1
                find = target - nums[i] - nums[j]
                while k < l: 
                    if nums[k] + nums[l] == find: 
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < len(nums) and nums[k] == nums[k-1]:
                            k += 1
                    elif nums[k] + nums[l] < find: 
                        k += 1
                    else: 
                        l -= 1
                j +=1
                while j < len(nums) and nums[j] == nums[j - 1]: 
                    j += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

        return res
