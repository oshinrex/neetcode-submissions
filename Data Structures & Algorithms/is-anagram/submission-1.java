class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] tracker = new int[26];

        for (int i = 0; i < s.length(); i++) {
            tracker[s.charAt(i)-'a']++;
            tracker[t.charAt(i)-'a']--;
        }

        for(int n : tracker) {
            if (n != 0) {
                return false;
            }
        }

        return true;
    }
}
