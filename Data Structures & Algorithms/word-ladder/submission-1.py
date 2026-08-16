class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # find adjacency list : key (pattern), values words that fit that pattern
        if endWord not in wordList: 
            return 0
        
        adj = {}
        adj_words = {}
        
        wordList.append(beginWord)
        for word in wordList: 
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern not in adj: 
                    adj[pattern] = []
                adj[pattern].append(word)
       
        # bfs
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q: 
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)): 
                    pattern = word[:j] + "*" + word[j+1:]
                    for w in adj[pattern]: 
                        if w not in visited: 
                            q.append(w)
                            visited.add(w)
            res += 1
        
        return 0