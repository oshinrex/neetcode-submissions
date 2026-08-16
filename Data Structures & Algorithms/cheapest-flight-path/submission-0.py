class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k+1):
            temp = dist.copy()
            for s, d, p in flights: 
                if dist[s] == float('inf'):
                    continue
                
                if p + dist[s] < temp[d]:
                    temp[d] = p + dist[s]
            dist = temp
                    
        return -1 if dist[dst] == float('inf') else dist[dst]
