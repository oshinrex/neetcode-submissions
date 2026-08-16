class Solution {
    public List<Integer> partitionLabels(String s) {
        // Hashmap to keep track of where last character is 
        // go through characters in string and keep track of 
        // length of parition

        HashMap<Character, Integer> map = new HashMap<>();
        List<Integer> ret = new ArrayList<>();
        int pointer = 0;
        int length = 0;

        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), i);
        }

        for (int i = 0; i < s.length(); i++) {
            System.out.println("pointer: " + pointer);
            System.out.println("i: " + i);
            System.out.println("Length: " + length);
            if (i > pointer) {
                ret.add(length);
                length = 1;
                pointer = map.get(s.charAt(i));
            } else {
                if (map.get(s.charAt(i)) > pointer) {
                    pointer = map.get(s.charAt(i));
                }
                length ++;
            }
        }

        ret.add(length);


        return ret;
    }
}
