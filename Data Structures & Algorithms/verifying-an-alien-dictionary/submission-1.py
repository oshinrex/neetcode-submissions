class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}

        for i in range(len(order)): 
            alphabet[order[i]] = i 

        for i in range(len(words) - 1): 
            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word2 == word1[:len(word2)]:
                return False

            for j in range(min(len(word1), len(word2))):
                if word1[j] == word2[j]:
                    continue 
                elif alphabet[word1[j]] < alphabet[word2[j]]:
                    break
                else: 
                    return False
        
        return True