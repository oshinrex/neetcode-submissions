class Solution {
    public boolean isValidSudoku(char[][] board) {
        // check rows and cols

        for (int i = 0; i < 9; i++) {
            HashSet<Character> rows = new HashSet<>();
            HashSet<Character> cols = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.' && !rows.add(board[i][j])) {
                    return false;
                }

                if (board[j][i] != '.' && !cols.add(board[j][i])) {
                    return false;
                }
            }
        }

        // check boxes 
        for (int k = 0; k < 9; k++) {
            HashSet<Character> box = new HashSet<>();
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if ((board[(k / 3) * 3 + i][(k % 3) * 3 + j] != '.') && !(box.add(board[(k / 3) * 3 + i][(k % 3) * 3 + j]))) {
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
