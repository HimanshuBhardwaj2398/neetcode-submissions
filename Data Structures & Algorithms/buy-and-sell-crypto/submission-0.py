class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       n= len(prices)
       max_prof=0
       for i in range(n):
        for j in range(i+1,n):
            max_prof=max(max_prof,prices[j]-prices[i])
       return max_prof

        