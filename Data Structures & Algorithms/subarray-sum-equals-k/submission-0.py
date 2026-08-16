class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        res = 0
        curSum = 0

        for n in nums: 
            curSum += n
            res += dct.get(curSum - k, 0)
            dct[curSum] = dct.get(curSum, 0) + 1

        return res