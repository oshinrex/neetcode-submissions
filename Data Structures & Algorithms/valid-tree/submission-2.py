class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adjacency list 
        adj = [[] for _ in range(n)]

        for i, j in edges: 
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()

        # dfs
        def dfs(i, j): 
            if i in visited: 
                return False
            
            visited.add(i)
            for curr in adj[i]: 
                if curr == j: 
                    continue 
                if not dfs(curr, i):
                    return False 
            return True 
        
        return dfs(0, -1) and len(visited) == n