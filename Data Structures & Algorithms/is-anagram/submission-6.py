class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        prevmapT={}
        prevmapS={}
        for i in t:
            prevmapT[i]=prevmapT.get(i,0)+1
        
        for i in s:
            if i in prevmapT:
                prevmapT[i]-=1
            else:
                return False
            if prevmapT[i]<0:
                return False
        return True