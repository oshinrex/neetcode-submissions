class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        
        Arrays.sort(nums); 
        System.out.println(Arrays.toString(nums));

        int longest = 1;
        int sequence = 1; 
        int prev = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == prev + 1) {
                sequence = sequence + 1;
                prev = nums[i];
            } else if (nums[i] == prev) {

            } else {
                longest = Math.max(longest, sequence);
                sequence = 1; 
                prev = nums[i];
            }
        }

        return Math.max(longest, sequence); 
    }
}
