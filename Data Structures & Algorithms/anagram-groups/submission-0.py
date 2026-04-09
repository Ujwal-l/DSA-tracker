class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevmap={}
        result=[]
        for s in strs:
            sorted_s=tuple(sorted(s))

            if sorted_s not in prevmap:
                prevmap[sorted_s]=[]
            prevmap[sorted_s].append(s)
        for value in prevmap.values():
            result.append(value)
        return result        