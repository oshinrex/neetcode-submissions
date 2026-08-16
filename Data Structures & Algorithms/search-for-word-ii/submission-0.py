class TrieNode:
    def __init__(self): 
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = TrieNode()
        
        def insert(head, word): 
            curr = head
            for c in word: 
                if c in curr.children: 
                    curr = curr.children[c]
                else: 
                    newNode = TrieNode()
                    curr.children[c] = newNode
                    curr = newNode
            curr.word = word

        for word in words: 
            insert(head, word)
        
        curr = head
        presentWords = []

        def dfs(r, c, node):
            if board[r][c] not in node.children:
                return 

            node = node.children[board[r][c]]
            
            if node.word:
                presentWords.append(node.word)
                node.word = None
            
            
            letter = board[r][c]
            board[r][c] = "#"

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for x, y in directions: 
                if 0 <= r + x < len(board) and 0 <= c + y < len(board[0]) and board[r + x][c + y] != "#": 
                    dfs(r + x, c + y, node)
            
            board[r][c] = letter 
        
        for r in range(len(board)): 
            for c in range(len(board[0])): 
                dfs(r, c, head)
        
        return presentWords




            
                