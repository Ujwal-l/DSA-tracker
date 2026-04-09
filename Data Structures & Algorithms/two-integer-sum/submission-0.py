class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap={}
        for index,num in enumerate(nums):
            diff=target-num
            if diff in prevmap:
                return[prevmap[diff],index]
            prevmap[num]=index
        