class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        path = []
        res = []

        def backtrack(i, curr_sum):
            nonlocal path
            nonlocal res
            if curr_sum == target: 
                res.append(path.copy())
                return 
            
            if i == len(nums) or curr_sum > target: 
                return 

            backtrack(i + 1, curr_sum)

            path.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            path.pop()
            
        backtrack(0, 0)
        return res