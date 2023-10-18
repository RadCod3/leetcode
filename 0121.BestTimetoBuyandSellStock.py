from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        curr_profit = 0
        l = n - 2
        r = n - 1

        while l >= 0:
            if prices[l] > prices[r]:
                r = l
                l -= 1
            else:
                curr_profit = max(curr_profit, prices[r] - prices[l])
                l -= 1

        return curr_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
