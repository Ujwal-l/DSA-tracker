class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {'}':'{',']':'[',')':'('}
        for c in s:
            if c in closetoopen:
                topElement = stack.pop() if stack else '#'
                if topElement != closetoopen[c]:
                    return False
            else:
                stack.append(c)
        return not stack
        
        