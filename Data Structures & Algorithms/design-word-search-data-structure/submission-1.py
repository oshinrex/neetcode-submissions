class Node:
    def __init__(self, val: str = ""):
        self.val = val 
        # key: letter, value : Node 
        self.neighbors = {}
        self.isEnd = False 


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word: 
            if c in curr.neighbors:
                curr = curr.neighbors[c]
            else: 
                curr.neighbors[c] = Node(c)
                curr = curr.neighbors[c]
        
        curr.isEnd = True 

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            if i == len(word):
                if node.isEnd:
                    return True 
                else: 
                    return False 
            
            if word[i] in node.neighbors:
                return dfs(i + 1, node.neighbors[word[i]])
            elif word[i] == '.': 
                for c in node.neighbors: 
                    if dfs(i + 1, node.neighbors[c]):
                        return True 
                return False 
            else: 
                return False 
        
        return dfs(0, self.root)

