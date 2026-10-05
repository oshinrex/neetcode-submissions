class Node:
    def __init__(self, val = ""):
        # key: val, val: node
        self.neighbors = {}
        self.words = set()
        self.val = val

class PrefixTree:

    def __init__(self):
        self.root = Node() 

    def insert(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            if word[i] in curr.neighbors: 
                curr = curr.neighbors[word[i]]
            else: 
                curr.neighbors[word[i]] = Node(word[i])
                curr = curr.neighbors[word[i]]
        
        curr.words.add(word)

    def search(self, word: str) -> bool:
        curr = self.root
        
        for i in range(len(word)): 
            if curr and word[i] in curr.neighbors:
                curr = curr.neighbors[word[i]]
            else:
                return False 
        
        if word in curr.words:
            return True 
        else: 
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for i in range(len(prefix)): 
            if curr and prefix[i] in curr.neighbors:
                curr = curr.neighbors[prefix[i]]
            else:
                return False 
        
        return True
        
        