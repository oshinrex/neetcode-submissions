class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        String longestSubstring = "";
        
        String longest = "";
        
        while (left <= right && right < s.length()) {
            if (longest.contains(String.valueOf(s.charAt(right)))) {
                if (longest.length() > longestSubstring.length()) {
                    longestSubstring = longest;
                    System.out.println(longestSubstring);
                }
                left = s.indexOf(s.charAt(right), left) + 1;
                right ++; 
                longest = s.substring(left, right);
            } else {
                longest = longest + String.valueOf(s.charAt(right));
                right ++;
            }
        }

        System.out.println(longestSubstring);
        return Math.max(longestSubstring.length(), longest.length());
    }
}
