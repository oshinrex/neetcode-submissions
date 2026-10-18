class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        path = []
        curr_sum = 0
        res = []

        def backtrack(i): 
            nonlocal res 
            nonlocal path
            nonlocal curr_sum 
            
            if curr_sum == target: 
                res.append(path.copy())
                return 
            
            if i == len(nums) or curr_sum > target: 
                return 
            
            backtrack(i + 1)
            path.append(nums[i])
            curr_sum += nums[i]
            backtrack(i)
            path.pop()
            curr_sum -= nums[i]
        
        backtrack(0)
        return res

            