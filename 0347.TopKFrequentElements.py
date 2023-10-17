from collections import defaultdict
from typing import List
from heapq import heapify, heappop, heappush, heapreplace


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)
        heap_list = []
        heapify(heap_list)

        for num in nums:
            num_counts[num] += 1

        for item in num_counts.items():
            item_ = (item[1] * -1, item[0])
            heappush(heap_list, item_)

        res = []
        for _ in range(k):
            a = heappop(heap_list)
            res.append(a[1])
        return res


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
