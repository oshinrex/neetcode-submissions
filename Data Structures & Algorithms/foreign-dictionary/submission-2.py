class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        for word in words:
            for ch in word:
                adj[ch] = []

        for i in range(len(words) - 1): 
            w1 = words[i]
            w2 = words[i+1]

            c = 0

            while c < len(w1) and c < len(w2) and w1[c] == w2[c]: 
                c += 1
            
            if c == len(w2) and c < len(w1):
                return ""
            
            if c < len(w1) and c < len(w2): 
                adj[w1[c]].append(w2[c])
        
        res = []
        visited = set()
        visiting = set()
        def dfs(i):
            if i in visiting: 
                return False

            if i in visited:
                return True 

            visiting.add(i)
            
            for c in adj[i]:
                if not dfs(c):
                    return False
            
            visiting.remove(i)
            visited.add(i)
            res.append(i)
            return True
        
        for i in adj: 
            if not dfs(i): 
                return ""
        
        return "".join(res[::-1])