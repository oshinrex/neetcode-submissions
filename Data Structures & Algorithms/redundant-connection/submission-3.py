class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [i for i in range(len(edges) + 1)]

        def find(i):
            if i == p[i]:
                return i 
            else: 
                return find(p[i])
            
        def union(i, j): 
            if find(i) == find(j):
                return False
            p[find(i)] = find(j)


            return True
        
        for i, j in edges: 
            if not union(i, j): 
                return [i, j]
        
        
        
