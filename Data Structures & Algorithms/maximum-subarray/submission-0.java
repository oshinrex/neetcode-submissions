class Solution {
    public int maxSubArray(int[] nums) {
        int sum = nums[0];
        int curr = sum;

        for (int i = 1; i < nums.length; i++) {
            System.out.println(sum);
            System.out.println(curr);
            sum = sum > curr ? sum : curr;
            if (curr < 0) {
                curr = nums[i];
            } else {
                curr += nums[i];
            }
        }

        return sum > curr ? sum : curr;
    }
}
