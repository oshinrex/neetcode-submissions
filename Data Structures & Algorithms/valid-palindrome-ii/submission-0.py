class Solution:
    def validPalindrome(self, s: str) -> bool:
        self.change = False
        def vp(l, r):
            if l >= r: 
                return True 

            if not s[l].isalnum():
                return vp(l + 1, r)
            elif not s[r].isalnum():
                return vp(l, r - 1)
            elif s[l] != s[r] and self.change:
                return False
            elif s[l] != s[r]:
                self.change = True
                return vp(l + 1, r) or vp(l, r - 1)
            else:
                return vp(l + 1, r - 1)
        
        return vp(0, len(s) - 1)