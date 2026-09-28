class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 1:
            return True 

        adj = {}

        for i in range(n): 
            adj[i] = []
        
        for e in edges: 
            i, j = e[0], e[1]
            adj[i].append(j)
            adj[j].append(i)
        
        seen = set()

        def dfs(i, prev): 
            nonlocal seen
            if i in seen: 
                return False 
            
            seen.add(i)

            for j in adj[i]:
                if j != prev: 
                    if not dfs(j, i):
                        return False
            
            return True 
        

        if not adj[0]:
            return False 
        
        if not dfs(0, -1): 
            return False
        
        if len(seen) != n:
            return False 
        
        return True 