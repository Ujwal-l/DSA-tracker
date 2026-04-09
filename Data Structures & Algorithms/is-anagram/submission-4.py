class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ps={}
        ts={}
        for i in s:
            ps[i]=ps.get(i,0)+1
        for i in t:
            if i not in ps or ps[i]<1:
                return False
            else:
                ps[i]-=1
        return True
