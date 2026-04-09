class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,a in enumerate(nums):
            if a==nums[i-1] and i>0:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                Threesum=a+nums[r]+nums[l]
                if Threesum>0:
                    r-=1
                elif Threesum<0:
                    l+=1
                else:
                    res.append([a,nums[r],nums[l]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res