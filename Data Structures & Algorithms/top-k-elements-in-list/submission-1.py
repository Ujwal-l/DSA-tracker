class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        prevmap = {}
        for i in nums:
            prevmap[i] = prevmap.get(i,0)+1

        sorted_prevmap = dict(sorted(prevmap.items(),key = lambda item:item[1],reverse=True))
        for i in range(k):
            res.append(list(sorted_prevmap)[i])
        return res

        