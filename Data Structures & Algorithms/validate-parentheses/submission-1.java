class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> stack = new ArrayList<>();

        HashMap<Character, Character> map = new HashMap<>();
        map.put('}', '{');
        map.put(']', '[');
        map.put(')', '(');

        for (int i = 0; i < s.length(); i++) {
            if (map.containsValue(s.charAt(i))) {
                stack.add(s.charAt(i));
            } 
            if (map.containsKey(s.charAt(i))) {
                if (stack.isEmpty()) {
                    return false;
                } 
                if (map.get(s.charAt(i)) == stack.get(stack.size() - 1)) {
                    stack.remove(stack.size() - 1);
                } else {
                    return false;
                }
            }
        }

        if (stack.isEmpty()) {
            return true;
        } else {
            return false;
        }


    }
}
