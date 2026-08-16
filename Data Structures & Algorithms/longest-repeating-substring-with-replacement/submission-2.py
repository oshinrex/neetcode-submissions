class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_val = 0

        char_map = {}

        for r in range(len(s)):
            char_map[s[r]] = char_map.get(s[r], 0) + 1

            while (r - l + 1) - max(char_map.values()) > k: 
                char_map[s[l]] -= 1
                l += 1
            max_val = max(max_val, r - l + 1)
        
        return max_val


