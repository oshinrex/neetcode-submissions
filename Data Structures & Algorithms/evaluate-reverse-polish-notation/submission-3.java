class Solution {
    public int evalRPN(String[] tokens) {
        int index = 0; 
        int prev1 = 0;
        int prev2 = 0;

        int currVal = 0;

        String operators = "+-*/";
        ArrayList<Integer> stack = new ArrayList<>();
        
        if (tokens.length == 1) {
            return Integer.parseInt(tokens[0]);
        }

        while (index < tokens.length) {
            if (operators.contains(String.valueOf(tokens[index]))) {
                prev2 = stack.remove(stack.size() - 1);
                prev1 = stack.remove(stack.size() - 1);

                if (String.valueOf(tokens[index]).equals("+")) {
                    currVal = prev1 + prev2;
                } else if (String.valueOf(tokens[index]).equals("*")) {
                    currVal = prev1 * prev2;
                } else if (String.valueOf(tokens[index]).equals("-")) {
                    currVal = prev1 - prev2;
                } else {
                    currVal = prev1 / prev2;
                }

                stack.add(currVal);

                System.out.println("currVal: " + currVal);
                System.out.println("prev1: " + prev1);

            } else {
                stack.add(Integer.parseInt(tokens[index]));
            }

            index ++;
        }

        return currVal;
    }
}
