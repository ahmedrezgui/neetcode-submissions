class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        l,r = 0, 1
        seen = {s[l]}
        res = 0

        while(r<len(s)):
            if ( s[r] in seen):
                res = max(res,len(seen))
                l+=1
                r = l+1
                seen = {s[l]}
            else:
                seen.add(s[r])
                r+=1
        return max(res,len(seen))