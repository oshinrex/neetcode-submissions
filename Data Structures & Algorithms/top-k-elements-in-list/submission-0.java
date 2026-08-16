class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer>[] lst = new ArrayList[nums.length];
        int[] returnArray = new int[k];

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            } else {
                map.put(nums[i], 1);
            }
            lst[i] = new ArrayList<>();
        }


        for (Integer key : map.keySet()) {
            lst[map.get(key) - 1].add(key);
        }

        int count = 0; 
        System.out.println(Arrays.toString(lst));

        for (int i = lst.length - 1; i >= 0; i--) {
            for (int j = 0; j <= lst[i].size() - 1; j++) {
                returnArray[count] = lst[i].get(j);
                count ++;
            }

            if (count == k) {
                return returnArray;
            }
        }

        return new int[0]; 
    }
}
