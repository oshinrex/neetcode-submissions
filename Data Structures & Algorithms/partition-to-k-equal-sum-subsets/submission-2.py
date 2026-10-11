class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        val = tot / k
        if tot % k != 0 or max(nums) > tot / k:
            return False 
        
        nums.sort(reverse = True)
        path = [0] * k

        def backtrack(i):
            seen = set()

            if i == len(nums):
                return True 
            
            for j in range(k):
                if path[j] + nums[i] > val or path[j] in seen:
                    continue 
                seen.add(path[j])
                path[j] += nums[i]
                if backtrack(i + 1):
                    return True 
                path[j] -= nums[i]
            
            return False
        
        return backtrack(0)