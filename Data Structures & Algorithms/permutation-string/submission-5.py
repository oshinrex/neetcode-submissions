class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        matches = 0
        lst_s1 = [0] * 26
        lst_s2 = [0] * 26

        for i in range(len(s1)):
            lst_s1[ord(s1[i]) - ord('a')] += 1
            lst_s2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if (lst_s1[i] == lst_s2[i]):
                matches += 1
        
        l = 1
        r = len(s1)

        while (r < len(s2)):
            if matches == 26: 
                return True
            
            if (lst_s2[ord(s2[l-1]) - ord('a')] == lst_s1[ord(s2[l-1]) - ord('a')]):
                matches -= 1
            lst_s2[ord(s2[l-1]) - ord('a')] -= 1
            if (lst_s2[ord(s2[l-1]) - ord('a')] == lst_s1[ord(s2[l-1]) - ord('a')]):
                matches += 1
            
            if (lst_s2[ord(s2[r]) - ord('a')] == lst_s1[ord(s2[r]) - ord('a')]):
                matches -= 1
            lst_s2[ord(s2[r]) - ord('a')] += 1
            if (lst_s2[ord(s2[r]) - ord('a')] == lst_s1[ord(s2[r]) - ord('a')]):
                matches += 1
            
            l += 1
            r += 1
            print(matches)
        
        if matches == 26:
            return True
        else:
            return False


            

        

        
        
        return False


