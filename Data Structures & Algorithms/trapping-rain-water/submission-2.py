class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        
        ret = 0

        maxLeft = height[l]
        maxRight = height[r]

        while (l != r):
            if maxLeft <= maxRight:
                l += 1
                if min(maxLeft, maxRight) - height[l] > 0:
                    ret += min(maxLeft, maxRight) - height[l]
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                if min(maxLeft, maxRight) - height[r] > 0:
                    ret += min(maxLeft, maxRight) - height[r]
                maxRight = max(maxRight, height[r])

        return ret 

