class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time = [float("inf")] * (n + 1)
        min_time[0] = 0
        min_time[k] = 0
        adj = {}

        for i, j, t in times: 
            if i not in adj:
                adj[i] = []
            
            if j not in adj: 
                adj[j] = []
            
            adj[i].append([j, t])

        marked = set()
        min_heap = [] 
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, [0, k])

        while min_heap: 
            val, node = heapq.heappop(min_heap)
            if val < min_time[node]:
                min_time[node] = val
            marked.add(node)
            for nei, t in adj[node]: 
                if nei not in marked: 
                    if min_time[node] + t < min_time[nei]:
                        min_time[nei] = min_time[node] + t
                        heapq.heappush(min_heap, [min_time[nei], nei])
        
        return -1 if max(min_time) == float("inf") else max(min_time)


        