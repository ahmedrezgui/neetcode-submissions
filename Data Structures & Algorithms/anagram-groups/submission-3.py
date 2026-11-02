class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            l = [0]*26
            for c in s:
                l[ord(c)-ord("a")]+=1
            hm[tuple(l)].append(s)
        return list(hm.values())