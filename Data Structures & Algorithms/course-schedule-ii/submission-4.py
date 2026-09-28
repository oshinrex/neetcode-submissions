class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj1 = {}
        adj2 = {}
        indegree = {}

        for i in range(numCourses):
            adj1[i] = []
            adj2[i] = []

        for p in prerequisites: 
            a, b = p[0], p[1]
             
            adj1[a].append(b)
            indegree[a] = indegree.get(a, 0) + 1

            adj2[b].append(a)
        
        q = deque()
        res = []

        for i in adj1:
            if not adj1[i]:
                q.append(i)
        
        while q: 
            curr = q.popleft() 
            res.append(curr)
            
            for a in adj2[curr]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)
        
        for a in indegree: 
            if indegree[a] != 0:
                return []
        
        return res