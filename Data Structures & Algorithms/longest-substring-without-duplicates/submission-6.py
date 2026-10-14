class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0  
        curr_len = 0
        longest = 0
        seen = set()

        for r in range(len(s)): 
            if s[r] in seen: 
                if curr_len > longest: 
                    longest = curr_len
                while s[r] in seen: 
                    seen.remove(s[l])
                    l += 1
                    curr_len -= 1
                seen.add(s[r])
                curr_len += 1
            else:
                curr_len += 1
                seen.add(s[r])
        
        return max(len(s) - l, longest)