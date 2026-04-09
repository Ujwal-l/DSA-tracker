class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        prevmap={}
        for i in s:
            prevmap[i]=prevmap.get(i,0)+1
        for char in t:
            if char not in prevmap  or prevmap[char]==0:
                return False
            prevmap[char]-=1
        return True