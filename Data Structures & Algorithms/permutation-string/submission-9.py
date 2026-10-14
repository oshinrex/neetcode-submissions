class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        matches = 0 

        lst1 = [0] * 26
        lst2 = [0] * 26

        for i in range(len(s1)): 
            lst1[ord(s1[i]) - ord('a')] += 1
            lst2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26): 
            if lst1[i] == lst2[i]: 
                matches += 1
        
        if matches == 26:
            return True 
        
        for i in range(len(s1), len(s2)): 
            l_c = s2[i - len(s1)]
            r_c = s2[i]

            if lst1[ord(l_c) - ord('a')] == lst2[ord(l_c) - ord('a')]:
                matches -= 1
            elif lst1[ord(l_c) - ord('a')] == lst2[ord(l_c) - ord('a')] - 1:
                matches += 1
            lst2[ord(l_c) - ord('a')] -= 1

            if lst1[ord(r_c) - ord('a')] == lst2[ord(r_c) - ord('a')]:
                matches -= 1
            elif lst1[ord(r_c) - ord('a')] == lst2[ord(r_c) - ord('a')] + 1:
                matches += 1
            lst2[ord(r_c) - ord('a')] += 1
        
            if matches == 26:
                return True 
        
        return False