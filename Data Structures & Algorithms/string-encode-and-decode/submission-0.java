class Solution {

    public String encode(List<String> strs) {
        String retString = "";
        for (int i = 0; i < strs.size(); i++) {
            retString += (strs.get(i).length() + "#" + strs.get(i));
        }

        return retString;
    }

    public List<String> decode(String str) {
        List<String> retLst = new ArrayList<>();
        int index = 0;

        while (index < str.length()) {
            String numb = "";
            while(str.charAt(index) != '#') {
                numb += str.charAt(index);
                index ++;
            }

            index ++;

            String word = "";
            for (int i = 0; i < Integer.valueOf(numb); i++) {
                word = word + str.charAt(index);
                index ++;
            }

            retLst.add(word);
        }
        
        return retLst;
    }
}
