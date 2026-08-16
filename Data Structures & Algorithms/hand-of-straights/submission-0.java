class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) {
            return false;
        }

        int min = hand[0];
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < hand.length; i++) {
            if (map.containsKey(hand[i])) {
                map.put(hand[i], map.get(hand[i]) + 1);
            } else {
                map.put(hand[i], 1);
            }
            min = min < hand[i] ? min : hand[i];
        }

        while (!map.isEmpty()) {
            for (int i = 0; i < groupSize; i++) {
                System.out.println(map);
                if (map.containsKey(min + i)) {
                    if (map.get(min + i) == 1) {
                        map.remove(min + i);
                    } else {
                        map.put(min + i, map.get(min + i) - 1);
                    }
                } else {
                    return false;
                }
            }
            if (map.isEmpty()) {
                return true;
            }
            min = Collections.min(map.keySet());
        }

        return true;

    }
}
