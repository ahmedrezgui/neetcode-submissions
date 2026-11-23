class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j=0
        res = ""
        while j< len(strs[0]):
            for i, s in enumerate(strs):
                if j>=len(s) or s[j]!=strs[0][j]:
                    return res
            res+=s[j]
            j+=1
        return res

