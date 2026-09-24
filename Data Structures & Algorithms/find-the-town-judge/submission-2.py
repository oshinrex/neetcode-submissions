class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # person a trust people b
        adj_lst = {}

        # person a is trust by people b
        lst2 = {}

        for r in trust: 
            p1, p2 = r[0], r[1]

            if p1 in adj_lst:
                adj_lst[p1].append(p2)
            else:
                adj_lst[p1] = [p2]

            if p2 not in adj_lst:
                adj_lst[p2] = []
            
            if p2 in lst2:
                lst2[p2].append(p1)
            else:
                lst2[p2] = [p1]
        
        for p in adj_lst: 
            if not adj_lst[p] and len(lst2[p]) == len(adj_lst) - 1:
                return p 
        
        return -1