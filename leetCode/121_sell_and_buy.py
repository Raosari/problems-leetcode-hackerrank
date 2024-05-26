# You are given an array prices where prices[i] 
# is the price of a given stock on the ith day.

# You want to maximize your profit by choosing 
# a single day to buy one stock and choosing a different day 
# in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        p = prices[0]
        for price in prices[1:]:
            if price > p:
                profit = price - p
                maxP = max(profit, maxP)
            else:
                p = price
        return maxP
    
    def maxProfit2(self,prices:List[int]):
        l = 0
        maxP = 0
        for r in range(len(prices)):
            value = prices[r] - prices[l]
            if value > 0:
                maxP = max(maxP,value)
            else:
                l = r
        return maxP

sol1 = Solution()
a = sol1.maxProfit2([7,1,5,3,6,0,200])
print(a)