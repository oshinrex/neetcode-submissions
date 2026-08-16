class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find all the o's in the border, add to queue 
        # dfs on all the o's in q
        # if connected, add to a list 
        # check every cell, if not in list, mark as x 
    
        q = deque() 
        connect = set()
        row, col = len(board), len(board[0])

        def dfs(r, c): 
            if r < 0 or c < 0 or r == row or c == col or board[r][c] == 'X' or (r, c) in connect: 
                return 
            connect.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for c in range(col): 
            dfs(0, c)
            dfs(row - 1, c)
        
        for r in range(1, row - 1): 
            dfs(r, 0)
            dfs(r, col - 1)
        
        for i in range(row):
            for j in range(col): 
                if board[i][j] == 'O' and (i, j) not in connect: 
                    board[i][j] = 'X'
        