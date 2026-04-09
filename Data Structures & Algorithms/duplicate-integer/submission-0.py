class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevmap={}
        for n in nums:
            prevmap[n]=prevmap.get(n,0)+1
        for key,value in prevmap.items():
            if value > 1:
                return True
        return False
        