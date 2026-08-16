class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int lefti = 0;
        int righti = matrix.length - 1;

        while (lefti <= righti) {
            int i = lefti + (righti - lefti);
            System.out.println("Here1");
            if (target >= matrix[i][0] && target <= matrix[i][matrix[0].length - 1]) {
                System.out.println("Here2");
                int l = 0;
                int r = matrix[0].length - 1;
                
                
                while (l <= r) {
                    System.out.println("Here");
                    int mid = l + (r - l)/2;
                    if (target == matrix[i][mid]) {
                        return true;
                    } else if (target < matrix[i][mid]) {
                        r = mid - 1;
                    } else {
                        l = mid + 1;
                    }
                }

                return false;

            } else if (target < matrix[i][0]) {
                righti = i - 1;
            } else {
                lefti = i + 1;
            }
        }

        return false;
    }
}
