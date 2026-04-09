class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,v in enumerate(temperatures):
            while stack and v>stack[-1][1]:
                stackInx,stackval = stack.pop()
                res[stackInx]=(i-stackInx)
            stack.append([i,v])
        return res

        