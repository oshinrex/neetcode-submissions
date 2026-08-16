class PrefixNode: 
    def __init__(self): 
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.head = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.head

        for c in word:
            if c not in curr.children: 
                new_curr = PrefixNode()
                curr.children[c] = new_curr
                curr = new_curr
            else:
                curr = curr.children[c]
        
        curr.endOfWord = True 

    def search(self, word: str) -> bool:
        curr = self.head 

        for c in word: 
            if c in curr.children:
                curr = curr.children[c]
            else: 
                return False
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.head 

        for c in prefix: 
            if c in curr.children:
                curr = curr.children[c]
            else: 
                return False
        
        return True
        