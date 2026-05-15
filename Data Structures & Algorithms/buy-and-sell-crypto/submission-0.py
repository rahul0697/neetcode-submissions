class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                p = sell-buy
                if r<p:
                    r = p
        return r