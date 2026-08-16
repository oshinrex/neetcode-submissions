class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): 
            return False
        
        d1 = [0] * 26
        d2 = [0] * 26

        for i in range(len(s1)): 
            d1[ord(s1[i]) - ord('a')] += 1

        matches = 0

        for i in range(26): 
            if d1[i] == d2[i]: 
                matches += 1
            
        l = 0

        for r in range(len(s2)): 
            print(matches)
            if matches == 26: 
                return True 
            
            if r - l == len(s1): 
                if d2[ord(s2[l]) - ord('a')] == d1[ord(s2[l]) - ord('a')]: 
                    matches -= 1

                d2[ord(s2[l]) - ord('a')] -= 1
                d2[ord(s2[r]) - ord('a')] += 1

                if d2[ord(s2[r]) - ord('a')] == d1[ord(s2[r]) - ord('a')]:
                    matches += 1
                l += 1
            else: 
                d2[ord(s2[r]) - ord('a')] += 1
                if d2[ord(s2[r]) - ord('a')] == d1[ord(s2[r]) - ord('a')]:
                    matches += 1
        
        if matches == 26: 
            return True
        else: 
            return False

