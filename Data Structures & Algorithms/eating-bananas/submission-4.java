public class Solution {
    public int minEatingSpeed(int[] piles, int h) {

        // merge sort 
        // mid = left + (right - left) / 2
        // while (left < right )
        // left = mid + 1
        // right = mid - 1
        int eating_rate = 0;
        int hours = piles.length;

        for (int i = 0; i < piles.length; i++) {
            if (piles[i] > eating_rate) {
                eating_rate = piles[i];
            }
        }

        if (eating_rate == 0) {
            return 0;
        }

        System.out.println(eating_rate);

        int left = 1;
        int right = eating_rate;

        while (left < right) {
            int mock_eating_rate = left + (right - left) / 2;
            System.out.println(mock_eating_rate);
            int count_hours = 0;
            
            for (int i = 0; i < piles.length; i++) {
                count_hours += (piles[i] / mock_eating_rate);
                if (piles[i] % mock_eating_rate != 0) {
                    count_hours ++;
                }
            }

            if (count_hours <= h) {
                right = mock_eating_rate;
                eating_rate = mock_eating_rate; 
            } else {
                left = mock_eating_rate + 1;
            }

        }

        return eating_rate;
    }
}
