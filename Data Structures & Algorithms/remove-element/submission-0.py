class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all occurrences of val form nums in-place
        last = len(nums) - 1
        i = 0

        while (i <= last):
            if (nums[i] == val):
                nums[i] = nums[last]
                last -= 1
            else:
                i += 1
        
        return last + 1