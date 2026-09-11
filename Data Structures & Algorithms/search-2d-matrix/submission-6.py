class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        
        res = []
        for i in matrix:
            if i[-1] < target or i[0] > target:
                continue
            else:
                res.append(i)

        if not res:
            return False
        nums = res.pop()
        right = len(nums)-1

        while left <=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                right = mid -1
            else:
                left = mid + 1
        return False       