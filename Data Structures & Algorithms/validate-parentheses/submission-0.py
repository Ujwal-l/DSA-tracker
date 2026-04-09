class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={')':'(',']':'[','}':'{'}
        for c in s:
            if c in closetoopen:
                top_element=stack.pop() if stack else "#"
                if closetoopen[c]!=top_element:
                    return False
            else:
                stack.append(c)
        return not stack
                
        
        