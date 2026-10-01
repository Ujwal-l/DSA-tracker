class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left =1
        right = max(piles)

        while left < right:
            mid = (left + right)//2

            hours = 0

            for k in piles:
                hours += (mid + k-1)//mid

            if hours > h:
                left = mid +1
            else:
                right = mid   
        return left    