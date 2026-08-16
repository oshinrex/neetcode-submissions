class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalidrome(l, r):
            while l < r: 
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r: 
            if s[l] != s[r]: 
                return isPalidrome(l, r - 1) or isPalidrome(l + 1, r)
            l += 1
            r -= 1
        
        return True