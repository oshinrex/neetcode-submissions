class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> retList = new ArrayList<>();
        int prev = 0;

        for (int i = 0; i < nums.length - 2; i++) {

            int left = i + 1; 
            int right = nums.length - 1; 

            while(left < right && (i == 0 || nums[i] != prev)) {
                int sum = nums[left] + nums[right] + nums[i];
                if (sum == 0) {
                    List<Integer> toAdd = new ArrayList<>();
                    toAdd.add(nums[i]); 
                    toAdd.add(nums[left]);
                    toAdd.add(nums[right]);

                    retList.add(toAdd);

                    int leftPrev = nums[left];
                    int rightPrev = nums[right];

                    while(left < nums.length && nums[left] == leftPrev) {
                        left ++;
                    }

                    while(right >= 0 && nums[right] == rightPrev) {
                        right --;
                    }

                } else if (sum < 0) {
                    left ++;

                } else {
                    right --;
                }
            }
            prev = nums[i];
            
        }

        return retList;
    }
}
