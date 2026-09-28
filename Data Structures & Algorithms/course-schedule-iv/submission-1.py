class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj1 = {}

        for i in range(numCourses):
            adj1[i] = set()

        for p in prerequisites:
            a, b = p[0], p[1]
            adj1[b].add(a)
        
        for i in range(numCourses):
            q = deque()
            visited = set()
            q.append(i)

            while q:
                curr = q.popleft()

                visited.add(curr)

                if curr != i:
                    adj1[i].add(curr)

                for j in adj1[curr]:
                    if j not in visited:
                        q.append(j)
                        adj1[i].add(j)
        
        res = [False] * len(queries)

        for i in range(len(queries)):
            uj, vj = queries[i][0], queries[i][1]

            if uj in adj1[vj]:
                res[i] = True
        
        return res