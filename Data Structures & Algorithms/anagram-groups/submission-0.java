class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ret = new ArrayList<>();
        List<String> first = new ArrayList<>();
        first.add(strs[0]);

        for (String s : strs) {
            boolean added = false;
            for (List<String> lst : ret) {
                if (lst.get(0).length() == s.length()) {
                    int[] alp = new int[26];

                    for (int i = 0; i < s.length(); i++) {
                        alp[s.charAt(i) - 'a']++;
                        alp[lst.get(0).charAt(i) - 'a']--;
                    }
                    
                    if (Arrays.equals(alp, new int[26])) {
                        lst.add(s);
                        added = true;
                        break;
                    } 
                }
            }

            if (!added) {
                List<String> toAdd = new ArrayList<String>();
                toAdd.add(s);
                ret.add(toAdd);
            }
        }
        return ret;
    }
}
