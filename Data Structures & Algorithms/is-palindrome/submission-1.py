class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = ''.join(char for char in s1 if char.isalnum())
        i, j = 0, len(s2)-1
        
        while (i < j and s2[j]==s2[i]):
            i+=1
            j-=1
        if i>=j:
            return True
        else:
            return False        
            
        
