"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        visited = [False]
        # cur = root
        while stack:
            cur, v = stack.pop(), visited.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    for child in reversed(cur.children):
                        stack.append(child)
                        visited.append(False)
                
        return res