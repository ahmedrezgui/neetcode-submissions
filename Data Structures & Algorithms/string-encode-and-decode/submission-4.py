class Solution:

    def encode(self, strs: List[str]) -> str:
        code= ""
        for s in strs:
            code+= str(len(s))+"#"+s
        return code

    def decode(self, s: str) -> List[str]:
        i= 0
        strs = []
        while i < len(s):
            l=""
            while s[i]!="#":
                l =l+s[i]
                i+=1
            i+=1
            l = int(l)
            strs.append(s[i:i+l])
            i = i+l

        return strs
        
