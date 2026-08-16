class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            lst = [0] * 26
            for l in s: 
                lst[ord(l) - ord('a')] += 1
            mp[tuple(lst)].append(s)
        
        return list(mp.values())