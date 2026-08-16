class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in n:
                c = nums[i]
                count = 0
                while c in n:
                    count += 1
                    c += 1
                longest = max(longest, count)
        
        return longest 