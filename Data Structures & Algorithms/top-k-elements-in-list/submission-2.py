class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        prevmap = {}
        for i in nums:
            prevmap[i] = prevmap.get(i,0)+1

        bucket = [[] for _ in range(len(nums)+1)]
        for key,count in prevmap.items():
            bucket[count].append(key)
        
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
 

        