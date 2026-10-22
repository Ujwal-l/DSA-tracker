class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r= max(weights),sum(weights)
        res = r

        def canShip(capacity):
            ships,currentload = 1,capacity

            for weight in weights:
                if currentload - weight < 0:
                    ships+=1
                    currentload = capacity
                currentload -= weight

            return ships <= days

        while l<=r:
            capacity = (l+r)//2
            if canShip(capacity):
                res= min(res,capacity)
                r= capacity - 1
            else:
                l = capacity +1

        return res
        