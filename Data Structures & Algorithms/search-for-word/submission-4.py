class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        marked = set()
        def dfs(i, j, n):
            if n == len(word):
                return True  
            if (i, j) in marked or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[n] != board[i][j]:
                return False
           
            marked.add((i, j))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            found = False

            for x, y in directions: 
                if dfs(i + x, j + y, n + 1): 
                    found = True

            marked.remove((i, j))    
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False
        