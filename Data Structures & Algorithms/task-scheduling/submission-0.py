class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        map = {}
        q = deque()
        time = 0
        i = 0
        
        for t in tasks: 
            map[t] = map.get(t, 0) - 1
            print("here")
        
        max_heap = list(map.values())     
        heapq.heapify(max_heap)

        while max_heap or q: 
            while q and q[0][1] == i: 
                freq, _ = q.popleft()
                heapq.heappush(max_heap, freq)
            if max_heap: 
                freq = heapq.heappop(max_heap)
                if freq < -1: 
                    q.append([freq + 1, i + n + 1])
            time += 1
            i += 1

        return time