class Solution(object):
    def maxProfit(self, prices):

        l, r = 0, 1
        max_stock = 0
        while r < len(prices):

            if (prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                max_stock = max(max_stock, profit)
            else:
                l = r
            r += 1
        return max_stock
