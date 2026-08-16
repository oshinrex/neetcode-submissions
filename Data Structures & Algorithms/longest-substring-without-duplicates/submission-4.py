class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0 

        l = 0 
        st = set()
        st.add(s[l])

        max_len = 1

        for r in range(1, len(s)): 
            if s[r] in st: 
                max_len = max(r - l, max_len)
                while s[r] in st: 
                    st.remove(s[l])
                    l += 1
            st.add(s[r]) 

        return max(max_len, len(s)-l)
