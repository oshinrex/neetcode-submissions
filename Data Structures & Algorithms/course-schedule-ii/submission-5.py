class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj2 = {}
        indegree = {}

        for i in range(numCourses):
            adj2[i] = []
            indegree[i] = 0

        for p in prerequisites: 
            a, b = p[0], p[1]
            
            indegree[a] = indegree.get(a, 0) + 1
            adj2[b].append(a)
        
        q = deque()
        res = []

        for i in indegree:
            if indegree[i] == 0:
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