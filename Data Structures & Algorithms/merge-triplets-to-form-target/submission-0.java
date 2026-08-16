class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        ArrayList<int[]> nums = new ArrayList<>();
        for (int[] tri : triplets) {
            if (tri[0] > target[0]) {
                continue;
            }

            if (tri[1] > target[1]) {
                continue;
            }

            if (tri[2] > target[2]) {
                continue;
            }

            nums.add(tri);
        }

        System.out.println(nums.size());

        boolean num1 = false;
        boolean num2 = false;
        boolean num3 = false;
        for (int[] tri : nums) {
            if (num1 && num2 && num3) {
                return true;
            }
            if (tri[0] == target[0]) {
                num1 = true;
            }

            if (tri[1] == target[1]) {
                num2 = true;
            }

            if (tri[2] == target[2]) {
                num3 = true;
            }
        }

        if (num1 && num2 && num3) {
                return true;
        }

        return false;
    }
}
