class TrieNode: 
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head 

        for c in word: 
            if c in curr.children: 
                curr = curr.children[c]
            else: 
                new_node = TrieNode()
                curr.children[c] = new_node
                curr = new_node
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root
            for i in range(j, len(word)): 
                if word[i] != ".": 
                    if word[i] in curr.children:
                        curr = curr.children[word[i]]
                    else:
                        return False
                else: 
                    for child in curr.children.values(): 
                        if dfs(i + 1, child): 
                            return True 
                    return False 
            return curr.endOfWord
        
        return dfs(0, self.head)

                    
