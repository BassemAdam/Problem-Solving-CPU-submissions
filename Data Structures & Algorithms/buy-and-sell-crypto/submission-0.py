class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        for L in range(len(prices)):
            for R in range(L+1,len(prices)):
                currProfit = prices[R] - prices[L]
                maxProfit = max(maxProfit,currProfit)
        return maxProfit