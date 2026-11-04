class Solution:
    def isValid(self, s: str) -> bool:
        if len (s)%2 != 0:
            return False

        stack = []
        for p in s:
            if p in ['(','[','{']:
                stack.append(p)  
            if p in [')',']','}']:
                if stack:
                    c = stack.pop(-1)
                    if (c== '(' and p==')') or (c == '{' and p=='}') or (c == '[' and p==']') :
                        continue
                    else:
                        return False    
                else :
                    return False

        if stack:
            return False                      
        return True