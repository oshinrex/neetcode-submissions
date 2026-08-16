class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}

        for i, j in prerequisites: 
            if i in prereq: 
                prereq[i].append(j)
            else:
                prereq[i] = [j]
            if j not in prereq:
                prereq[j] = []
        
        visited = set()

        def dfs(curr): 
            if curr in visited: 
                return False
            if prereq[curr] == []:
                return True
            
            visited.add(curr)
            for p in prereq[curr]: 
                if not dfs(p):
                    return False
            visited.remove(curr)
            prereq[curr] = []
            return True

        for curr in prereq: 
            if not dfs(curr):
                return False
        
        return True
                