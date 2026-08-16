class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> set = new HashMap<>();
        int[] retArray = new int[2];

        for (int i = 0; i < numbers.length; i++) {
            if (set.containsKey(target - numbers[i])) {
                retArray[0] = set.get(target - numbers[i]);
                retArray[1] = i+1;
                return retArray;
            } else {
                set.put(numbers[i], i+1);
            }
        }

        return retArray;
    }
}
