class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sort = []
        res = []
        heapq.heapify(sort)

        for n in nums:
            heapq.heappush(sort, n)
        
        for _ in range(len(sort)):
            res.append(heapq.heappop(sort))
        
        return res