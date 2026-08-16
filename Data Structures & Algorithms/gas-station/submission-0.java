class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int sum = 0;
        for (int i = 0; i < gas.length; i++) {
            sum += gas[i] - cost[i];
        }
        
        if (sum < 0) {
            return -1;
        }


        int ret = 0;
        int mon = 0;
        for (int i = 0; i < gas.length; i++) {
            if (mon + (gas[i] - cost[i]) < 0) {
                mon = 0;
                ret = i + 1;
            } else {
                mon = mon + gas[i] - cost[i];
            }
        }

        return ret;
    }
}
