class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_sort=sorted(nums)
        return nums_sort[0]


        # l=0
        # r=len(nums_sort)-1
        # while l<=r:
        #     mid=(left+right)//2
        #     if nums[mid]<nums[mid+1]:
        #         mid=