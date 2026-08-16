class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        retArr = [0] * (2 * len(nums))

        for i in range(len(nums)):
            retArr[i] = nums[i]
            retArr[i + len(nums)] = nums[i]
        
        return retArr
        