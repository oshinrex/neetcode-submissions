class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}

        for i, c in enumerate(order):
            rank[c] = i

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]

            if len(w2) < len(w1) and w2 == w1[:len(w2)]:
                return False 
            
            for j in range(min(len(w1), len(w2))):
                if rank[w1[j]] == rank[w2[j]]:
                    continue 
                elif rank[w1[j]] < rank[w2[j]]:
                    break 
                else: 
                    return False 
            
        return True 