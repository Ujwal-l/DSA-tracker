class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevmap={}
        for i in nums:
            prevmap[i]=prevmap.get(i,0)+1

        for val in prevmap.values():
            if val > 1:
                return True
        return False
        