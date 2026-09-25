class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j): 
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O": 
                return 

            board[i][j] = "T"

            for x, y in dir: 
                nx = i + x
                ny = j + y 
                dfs(nx, ny)
        
        for i in range(len(board)): 
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
                
