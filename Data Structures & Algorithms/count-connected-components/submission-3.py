class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mp = {}
        for i in range(n):
            mp[i] = set()
        
        for e in edges: 
            a, b = e[0], e[1]
            mp[a].add(b)
            mp[b].add(a)
        
        seen = set()
        res = 0 

        def dfs(n):
            seen.add(n)

            for i in mp[n]:
                if i not in seen: 
                    dfs(i)

        for n in mp: 
            if n in seen: 
                continue 
            
            dfs(n)
            res += 1
        
        return res