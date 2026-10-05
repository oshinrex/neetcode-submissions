class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []

        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        
        self.k = k
        print(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            if val <= self.heap[0]:
                return self.heap[0]
            else:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
                return self.heap[0]
        else:
            heapq.heappush(self.heap, val)
            return self.heap[0]
