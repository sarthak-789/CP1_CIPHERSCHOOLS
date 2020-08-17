# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=sys.maxsize
        mx=0
        for i in range(len(prices)):
                if prices[i]< mn:
                    mn=prices[i]
                if prices[i]-mn>mx:
                    mx=prices[i]-mn
        return mx
                