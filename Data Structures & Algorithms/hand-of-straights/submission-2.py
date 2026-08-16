class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize != 0 or len(hand) < groupSize):
            return False
        
        cards = {}

        for i in range(len(hand)):
            cards[hand[i]] = cards.get(hand[i], 0) + 1
        
        minH = list(cards.keys())

        heapq.heapify(minH)

        while minH: 
            min_card = minH[0]
            count = min_card

            for i in range(groupSize):
                if (count not in cards or cards[count] == 0):
                    return False
                if (cards[count] - 1 == 0):
                    heapq.heappop(minH)
                cards[count] -= 1
                count += 1
        
        
        return True


