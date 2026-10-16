class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best,buy=0,0
        for sell in range(1,len(prices)):
            if prices[sell]< prices[buy]:
                buy=sell
            else:
                best=max(best,prices[sell]-prices[buy])
        return best




        