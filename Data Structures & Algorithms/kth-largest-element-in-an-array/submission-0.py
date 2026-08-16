class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        heapq.heapify(res)

        for n in nums: 
            if len(res) < k: 
                heapq.heappush(res, n)
            else:
                if res[0] < n: 
                    heapq.heappop(res)
                    heapq.heappush(res, n)
        
        return res[0]