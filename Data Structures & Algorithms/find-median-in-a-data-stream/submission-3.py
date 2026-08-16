class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap, -num)

        heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))

        if len(self.left_heap) < len(self.right_heap): 
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
        

    def findMedian(self) -> float:
        if (len(self.left_heap) + len(self.right_heap)) % 2: 
            return -self.left_heap[0]
        return (-self.left_heap[0] + self.right_heap[0])/2