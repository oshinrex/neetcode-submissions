class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag = set()
        negDiag = set()
        col = set()

        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def backtrack(i):
            if i == n: 
                res.append(["".join(row) for row in board])
                return 
            
            for j in range(n):
                if i+j in posDiag or i-j in negDiag or j in col:
                    continue 
                
                posDiag.add(i+j)
                negDiag.add(i-j)
                col.add(j)
                board[i][j] = "Q"

                backtrack(i + 1)

                posDiag.remove(i+j)
                negDiag.remove(i-j)
                col.remove(j)
                board[i][j] = "."
        
        backtrack(0)
        return res

                