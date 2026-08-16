class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()
        visiting = set()
        num = 0

        def dfs(i): 
            if i in visited: 
                return
            visiting.add(i)
            visited.add(i)

            for j in adj[i]:
                dfs(j)
            visiting.remove(i)
            return 
        
        for i in range(len(adj)): 
            if i not in visited:
                dfs(i)
                num += 1
        
        return num