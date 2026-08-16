class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = [[] for _ in range(numCourses)]

        for i, j in prerequisites: 
            prereq[i].append(j)
        
        visited = set()
        visiting = set()
        order = []

        def dfs(i):
            if i in visiting: 
                return False
            
            if i in visited: 
                return True 
            
            visiting.add(i)
            for j in prereq[i]: 
                if not dfs(j):
                    return False
            order.append(i)
            visiting.remove(i)
            visited.add(i)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        if i not in visited: 
            order.append(i)

        return order