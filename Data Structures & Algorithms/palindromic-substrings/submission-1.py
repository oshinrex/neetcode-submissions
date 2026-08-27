class Solution:
    def countSubstrings(self, s: str) -> int:
        tot = 0 
        
        for i in range(len(s)): 
            # if s is the center of palindrome
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                tot += 1
                l -= 1
                r += 1

            # is s is the left of the center 
            l, r = i, i + 1

            while l >= 0 and  r < len(s) and s[l] == s[r]:
                tot += 1
                l -= 1
                r += 1
        
        return tot