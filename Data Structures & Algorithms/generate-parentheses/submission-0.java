class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> retList = new ArrayList<>();
        String res = "";

        backtrack(0, 0, n, retList, res);
        return retList;
    }
}

public void backtrack(int openN, int closeN, int n, List<String> retList, String res) {
    if (openN == n && closeN == n) {
        retList.add(res);
    } 

    if (closeN < openN) {
        backtrack(openN, closeN + 1, n, retList, res + ")");
    }

    if (openN < n) {
        backtrack(openN + 1, closeN, n, retList, res + "(");
    }
}