class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0]*26
        for c in s:
            l[ord(c)-ord("a")]+=1
        for c in t:
            l[ord(c)-ord("a")]-=1
        for i in l:
            if i !=0: return False
        return True

        