class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] retArray = new int[temperatures.length];
        ArrayList<Integer> stack = new ArrayList<>();
        ArrayList<Integer> indicies = new ArrayList<>();

        for (int i = 0; i < temperatures.length; i++) {
            boolean condition = true;
            while (!stack.isEmpty() && condition == true) {
                if (stack.get(stack.size() - 1) < temperatures[i]) {
                    retArray[indicies.get(stack.size() - 1)] = i - indicies.get(stack.size() - 1);
                    stack.remove(stack.size() - 1);
                    indicies.remove(indicies.size() - 1);
                } else {
                    condition = false;
                }
            }
            stack.add(temperatures[i]); 
            indicies.add(i);
        }

        return retArray;
    }
}
