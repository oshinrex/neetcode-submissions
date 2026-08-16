class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            ind = i
            while stack and stack[-1][0] > heights[i]:
                val, pos = stack.pop()
                max_area = max(max_area, val * (i - pos))
                ind = pos
            stack.append((heights[i], ind))

        while (stack):
            height, pos = stack.pop()
            max_area = max(max_area, height * (len(heights) - pos))

        return max_area