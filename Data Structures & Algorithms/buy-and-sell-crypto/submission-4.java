class Solution {
    public int maxProfit(int[] prices) {
        //prices=[5,1,5,6,7,1,10]
        int left = 0;
        int right = 1;
        int maxProfit = 0;
        while (left < right && right <= prices.length - 1) {
            maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
            if (prices[left] < prices[right]) {
                right ++;
            } else {
                left = right;
            }

            if (left == right) {
                right ++;
            }

        }

        return maxProfit;
    }
}
