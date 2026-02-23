from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        opens =  '([{'
        closes = ')]}'
        stack = deque()
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != opens[closes.find(c)]:
                    return False
        if not stack:
            return True
        return False