class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevmap={}
        res=[]
        for s in strs:
            sorted_s=tuple(sorted(s))
            if sorted_s not in prevmap:
                prevmap[sorted_s]=[]
            
            prevmap[sorted_s].append(s)
        for i in prevmap.values():
            res.append(i)
        return res


        