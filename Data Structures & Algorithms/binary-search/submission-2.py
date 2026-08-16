class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r: 
            mid = (r + l) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]: 
                r = mid - 1
            else: 
                l = mid + 1
        
        if nums[l] == target: 
            return l
        else: 
            return -1
