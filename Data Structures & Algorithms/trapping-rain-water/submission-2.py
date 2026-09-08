class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        leftMax,rightMax = height[left],height[right]
        res = 0 
        while left < right:
            if leftMax<rightMax:
                left +=1
                if leftMax - height[left]>0:
                    res+=leftMax-height[left]
                leftMax=max(leftMax,height[left])
            else:
                right-=1
                if rightMax-height[right]>0:
                    res+=rightMax-height[right] 
                rightMax= max(rightMax,height[right])
        return res
        