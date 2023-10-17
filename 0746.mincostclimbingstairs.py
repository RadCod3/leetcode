from typing import List
from functools import lru_cache


@lru_cache(maxsize=None)
def minCostRec(cost, i=0):
    if i >= len(cost):
        return 0
    elif i == len(cost) - 1:
        return cost[i]
    else:
        return cost[i] + min(minCostRec(cost, i + 1), minCostRec(cost, i + 2))


def minCostClimbingStairs(cost: List[int]) -> int:
    return min(minCostRec(cost, 0), minCostRec(cost, 1))


print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
