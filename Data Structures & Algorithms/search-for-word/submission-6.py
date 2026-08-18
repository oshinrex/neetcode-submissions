class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, c): 
            if c == len(word): 
                return True 
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[c] != board[i][j]: 
                return False
            
            board[i][j] = "#"
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for x, y in directions: 
                if dfs(i + x, j + y, c + 1): 
                    board[i][j] = word[c]
                    return True 
            board[i][j] = word[c]
            return False 
        
        for i in range(len(board)):
            for j in range(len(board[0])): 
                if dfs(i, j, 0): 
                    return True 
        
        return False