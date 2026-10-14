class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        l = 0 
        max_sub = 0 
        max_freq = 0

        for r in range(len(s)): 
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            if freq[s[r]] > max_freq:
                max_freq = freq[s[r]]
            
            while (r - l + 1 - max_freq) > k: 
                freq[s[l]] -= 1
                l += 1

            max_sub = max(max_sub, r - l + 1)

        return max_sub