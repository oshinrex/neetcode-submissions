class Solution {
    public int[] productExceptSelf(int[] nums) {    
        int[] leftArray = new int[nums.length];
        int[] rightArray = new int[nums.length];
        int[] retArray = new int[nums.length];

        leftArray[0] = 1;
        rightArray[nums.length - 1] = 1;
        int productl = 1;
        int productr = 1;

        for (int i = 1; i < nums.length; i++) {
            leftArray[i] = productl * nums[i-1];
            rightArray[nums.length - i - 1] = productr * nums[nums.length - i];

            productl = leftArray[i];
            productr = rightArray[nums.length - i - 1];
        }

        for (int i = 0; i < nums.length; i++) {
            retArray[i] = leftArray[i] * rightArray[i];
        }

        return retArray;
    }
}  
