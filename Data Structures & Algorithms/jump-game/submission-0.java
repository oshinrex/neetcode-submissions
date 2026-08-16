class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 1) {
            return true;
        }

        int length = 1;

        for (int i = nums.length - 2; i > 0; i--) {
            if (nums[i] < length) {
                length ++;
            } else {
                length = 1;
            }

            System.out.println(length);
        }

        return nums[0] >= length ? true : false;
    }
}
