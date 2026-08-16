class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (n * 2)

        for i, num in enumerate(nums): 
            res[i] = num
            res[i + n] = num
        
        return res