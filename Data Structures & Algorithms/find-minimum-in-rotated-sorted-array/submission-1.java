class Solution {
    public int findMin(int[] nums) {
        // left, right 
        // while (left < right)
            // mid = left + (right - left) / 2
            // if (search <= mid) {
                // right = mid
            //} else {
            //  // left = mid + 1;
            //} 
        
        int left = 0;
        int right = nums.length;
        int min = nums[0];
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= min) {
                right = mid; 
                min = nums[mid];
            } else {
                left = mid + 1;
            }
        }

        return min;
    }
}
