class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={']':'[','}':'{',')':'('}
        for c in s:
            if c in closetoopen:
                top_element=stack.pop() if stack else "#"
                if top_element!=closetoopen[c]:
                    return False

            else:
                stack.append(c)
        return not stack
