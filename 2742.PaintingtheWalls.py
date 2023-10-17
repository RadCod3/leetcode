from typing import List
from functools import cache


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        # https://www.youtube.com/watch?v=qMZJunF5UaI
        # The main observation here is the fact that during the time the paid painter is painting
        # the free painter can paint walls. So if paid painter paints the ith wall, it takes him
        # time[i] time. Therefore the free painter can clear out time[i] walls during that time
        # since he can paint a wall in 1 unit time. And the remaining wall count would be,
        # remaining walls minus 1 that the paid painter paints and minus the amount of walls the
        # free paininter paints which is time[i]. I.e. remaining = remaining - 1 - time[i]
        # this will end up giving negative values for remaining but that is ok and it can be our
        # base case.
        @cache
        def paintWallsRec(i: int, remaining: int):
            if remaining <= 0:
                return 0

            if i >= n:
                return float("inf")

            # paid painter paints ith wall
            chose_i = cost[i] + paintWallsRec(i + 1, remaining - time[i] - 1)

            # paid painter does not paint ith wall
            not_chose_i = paintWallsRec(i + 1, remaining)

            return min(chose_i, not_chose_i)

        return paintWallsRec(0, n)


sol = Solution()
print(sol.paintWalls([1, 2, 3, 2], [1, 2, 3, 2]))
