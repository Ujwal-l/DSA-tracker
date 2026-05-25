class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prevmap={}
        n=len(nums)
        for i in nums:
            prevmap[i]=prevmap.get(i,0)+1
        for key,val in prevmap.items():
            if val>(n/2):
                return key
        