class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for w in strs:
            count=[0]*26
            for c in w:
                count[ord(c)-ord('a')] +=1
            if tuple(count) not in hashMap:
                hashMap[tuple(count)]= [w]
            else:        
                hashMap[tuple(count)].append(w)
    
        return list(hashMap.values())        