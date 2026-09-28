class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_lst = {}
        adj_lst2 = {}
        num_courses = 0 

        for p in prerequisites: 
            a, b = p[0], p[1]
            
            if a in adj_lst: 
                adj_lst[a].append(b)
            else: 
                adj_lst[a] = [b]
                num_courses += 1
            
            if b not in adj_lst: 
                adj_lst[b] = []
                num_courses += 1
            
            if b in adj_lst2: 
                adj_lst2[b].append(a)
            else: 
                adj_lst2[b] = [a]
            
            if a not in adj_lst2:
                adj_lst2[a] = []
        
        q = deque()

        for a in adj_lst: 
            if not adj_lst[a]:
                q.append(a)
                num_courses -= 1

        while q: 
            curr = q.popleft() 

            for n in adj_lst2[curr]: 
                adj_lst[n].remove(curr)
                if not adj_lst[n]: 
                    q.append(n)
                    num_courses -= 1
        
        return num_courses == 0
            

        
