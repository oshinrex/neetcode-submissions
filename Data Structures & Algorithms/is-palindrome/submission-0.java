class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        String str = s.toLowerCase(); 

        String alphabet = "abcedfghijklmnopqrstuvwxyz0123456789";

        while (left <= right) {
            if (alphabet.contains(String.valueOf(str.charAt(left))) && alphabet.contains(String.valueOf(str.charAt(right)))) {
                System.out.println(s.charAt(left));
                System.out.println(s.charAt(right));
                System.out.println();
                if (str.charAt(left) != str.charAt(right)) {
                    return false;
                } 
                left ++;
                right --;
            } else {
                if (!alphabet.contains(String.valueOf(str.charAt(left)))) {
                    left ++;
                }
                if (!alphabet.contains(String.valueOf(str.charAt(right)))) {
                    right --;
                }
            }
        }

        return true;
    }
}
