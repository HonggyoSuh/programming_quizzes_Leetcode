from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if prices == sorted(prices):
        #     return prices[len(prices) - 1] - prices[0]
        # if prices == sorted(prices, reverse = True):
        #     return 0
        # if len(prices) == 1:
        #     return 0

        # profit = 0
        # for index, i in enumerate(prices):
        #     if index + 1 < len(prices):
        #         profit = max(profit, max(prices[index + 1 :]) - i)

        # return profit

        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return max_profit
