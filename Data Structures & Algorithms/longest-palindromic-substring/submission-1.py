class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = ""
        num_char = 0

        for i in range(len(s)): 

            l, r = i, i
            # odd 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if num_char < r - l + 1:
                    num_char = r - l + 1
                    longest_str = s[l:r+1]
                l -= 1
                r += 1

            #even 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if num_char < r - l + 1:
                    num_char = r - l + 1
                    longest_str = s[l:r+1]
                l -= 1
                r += 1

        return longest_str