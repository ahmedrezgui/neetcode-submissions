class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(","{","["]:
                stack.append(c)
            elif c in [")","]","}"]:
                if (len(stack)==0) or (c ==")" and stack[-1]!="(") or (c =="]" and stack[-1]!="[") or (c =="}" and stack[-1]!="{"):
                    return False
                else:
                    stack.pop()
        if len(stack)==0:
            return True
        return False
