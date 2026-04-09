class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prevmap={}
        m=len(nums)/2
        for c in nums:
            prevmap[c]=prevmap.get(c,0)+1
        for key, values in prevmap.items():
            if values>m:
                return key
        