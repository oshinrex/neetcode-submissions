class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ret = [0] * (len(nums) - k + 1)

        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            
            if q[0] <= i - k:
                q.popleft()
            
            if i >= k - 1:
                ret[i - k + 1] = nums[q[0]]

        return ret
