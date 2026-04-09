class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        l,r=0,1
        while r<len(temperatures):
            if temperatures[r]>temperatures[l]:
                res.append(r-l)
                l+=1
                r=l+1
            else:
                r+=1
            if r==len(temperatures):
                res.append(0)
                l+=1
                r=l
        return res        