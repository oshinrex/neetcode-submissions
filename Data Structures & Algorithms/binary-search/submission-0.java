class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while(left <= right) {
            if (target == nums[left + (right - left)/2]) {
                return left + (right - left)/2;
            } else if (target > nums[left + (right - left)/2]) {
                left = left + (right - left)/2 + 1;
            } else {
                right = left + (right - left)/2 - 1;
            }
        }

        return -1;
    }
}
