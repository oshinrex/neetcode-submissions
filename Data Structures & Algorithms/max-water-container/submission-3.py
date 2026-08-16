class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r: 
            if heights[l] <= heights[r]: 
                maxArea = max(maxArea, (r - l) * heights[l])
                l += 1
            else: 
                maxArea = max(maxArea, (r - l) * heights[r])
                r -= 1
        
        return maxArea