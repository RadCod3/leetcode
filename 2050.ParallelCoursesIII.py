from collections import defaultdict
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        for u, v in relations:
            adj[u].append(v)

        max_time = {}

        def dfs(u):
            if u in max_time:
                return max_time

            res = time[u - 1]
            for v in adj[u]:
                res = max(dfs(v) + time[u - 1], res)
            max_time[u] = res
            return res

        for i in range(1, n + 1):
            dfs(i)

        return max(max_time.values())
