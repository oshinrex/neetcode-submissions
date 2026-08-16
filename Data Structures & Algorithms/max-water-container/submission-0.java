class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxArea = 0; 

        while (left < right) {
            int temp = (right - left) * Math.min(heights[left], heights[right]);
            maxArea = Math.max(maxArea, temp);

            if (heights[left] < heights[right]) {
                left ++;
            } else {
                right --;
            }
        }

        return maxArea;
    }
}
