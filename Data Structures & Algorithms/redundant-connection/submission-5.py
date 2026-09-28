class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegree = {}
        adj_lst = {}

        for e in edges:
            a, b = e[0], e[1]
            
            if a in adj_lst:
                adj_lst[a].append(b)
            else:
                adj_lst[a] = [b]
            
            if b in adj_lst:
                adj_lst[b].append(a)
            else:
                adj_lst[b] = [a]
            
            indegree[a] = indegree.get(a, 0) + 1
            indegree[b] = indegree.get(b, 0) + 1

        q = deque() 

        for a in indegree: 
            if indegree[a] == 1: 
                q.append(a)
        
        while q: 
            curr = q.popleft()
            indegree[curr] -= 1
            for a in adj_lst[curr]:
                indegree[a] -= 1
                if indegree[a] == 1: 
                    q.append(a)
            
        for i in range(len(edges) - 1, -1, -1):
            a, b = edges[i][0], edges[i][1]

            if indegree[a] > 0 and indegree[b] > 0: 
                return [a, b]
        
