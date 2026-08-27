class Solution:
    def longestPalindrome(self, s: str) -> str:
        # define dp[i] to be the longest palidrome with that index as the center or that index as the left middle point

        if not s: 
            return 0 

        if len(s) == 1: 
            return s[0]

        dp = [0] * len(s)
        longest = 0 
        res = ""
        
        for i in range(len(s)):
            # check if ith index is center 
            curr_len = 1
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len += 2
                l -= 1
                r += 1
            
            if curr_len > longest: 
                longest = curr_len 
                res = s[l + 1: r]
            
            # check if ith index is left 
            curr_len = 0
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len += 2
                l -= 1
                r += 1
            
            if curr_len > longest: 
                longest = curr_len 
                res = s[l + 1: r]
        
        return res