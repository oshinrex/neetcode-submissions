class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = [0] * len(height), [0] * len(height)
        max_area = 0

        l = 1
        maxl = height[0]
        while l < len(height):
            max_l[l] = maxl
            maxl = max(maxl, height[l])
            l += 1
        
        r = len(height) - 2
        maxr = height[len(height) - 1]
        while r > -1: 
            max_r[r] = maxr
            maxr = max(maxr, height[r])
            r -= 1

        print(max_l)
        print(max_r)
        
        for i in range(len(height)): 
            if (min(max_r[i], max_l[i]) - height[i]) > 0: 
                max_area += min(max_r[i], max_l[i]) - height[i]
        
        return max_area



