class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] retArray = new int[nums.length];
        int totalProduct = 1;

        for (int i = 0; i < nums.length; i++) {
            totalProduct = totalProduct * nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                int pro = 1;
                for (int j = 0; j < nums.length; j++) {
                    if (i != j) {
                        pro = pro * nums[j];
                    }
                }
                retArray[i] = pro;
            } else {
                retArray[i] = totalProduct / nums[i];
            }
        }

        return retArray;
    }
}  
