class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevmap={}
        for i,v in enumerate(numbers):
            diff=target-v
            if diff in prevmap:
                return [prevmap[diff]+1,i+1]
            prevmap[v]=i
        