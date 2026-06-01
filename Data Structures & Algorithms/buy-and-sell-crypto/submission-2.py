class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxprofit=0
        for r in range(1,len(prices)):
            if prices[l]>prices[r]:
                l=r
            else:
                curr_profit=prices[r]-prices[l]
                maxprofit=max(maxprofit,curr_profit)
        return maxprofit         
        