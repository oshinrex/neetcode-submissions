class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap, -num)
        if self.left_heap and self.right_heap: 
            while self.right_heap and -self.left_heap[0] > self.right_heap[0]: 
                heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
        
        while len(self.left_heap) - len(self.right_heap) > 1: 
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))

    def findMedian(self) -> float:
        if (len(self.left_heap) + len(self.right_heap)) % 2: 
            return -self.left_heap[0]
        else: 
            return (-self.left_heap[0] + self.right_heap[0])/2