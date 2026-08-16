class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create adjacency list 
        adj = collections.defaultdict(list)

        for src, dst in sorted(tickets, reverse = True): 
            adj[src].append(dst)
        
        res = []

        def backtrack(src):
            while adj[src]: 
                nxt = adj[src].pop()
                backtrack(nxt)
            res.append(src)
        
        backtrack("JFK")
        return res[::-1]
