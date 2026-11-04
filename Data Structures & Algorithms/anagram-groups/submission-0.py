class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        sort = ["".join(sorted(s)) for s in strs]
        for i , s in enumerate(sort):
            if s in hashmap:
                hashmap[s].append(strs[i])
            else:
                hashmap[s] = [strs[i]]
        values = list(hashmap.values())             
        return values

