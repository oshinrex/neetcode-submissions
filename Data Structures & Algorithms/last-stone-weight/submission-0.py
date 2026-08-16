class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = stones

        for i in range(len(stones)): 
            new_stones[i] = -1 * stones[i]

        heapq.heapify(new_stones)   

        while len(new_stones) > 1: 
            stone1 = heapq.heappop(new_stones)
            stone2 = heapq.heappop(new_stones)
            if stone1 < stone2:
                heapq.heappush(new_stones, stone1 - stone2) 
        
        if len(new_stones):
            return -1 * new_stones[0]
        else:
            return 0