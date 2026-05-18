class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        prevs={}
        for i in s:
            prevs[i]=prevs.get(i,0)+1
        for j in t:
            if j in prevs:
               prevs[j]-=1
            else:
                return False

            if prevs[j]<0:
                return False
        return True


        