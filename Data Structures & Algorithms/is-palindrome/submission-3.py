class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([c for c in s if c.isalnum()])
        i, j= 0, len(s)-1
        while i<=j and s[i]==s[j]:
            i+=1
            j-=1
        if i>j:
            return True
        return False
