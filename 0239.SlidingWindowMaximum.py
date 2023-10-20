from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        outputs = []
        d = deque()

        l = r = 0

        while r < len(nums):
            while d and nums[d[-1]] < nums[r]:
                d.pop()

            d.append(r)

            if l > d[0]:
                d.popleft()

            if (r + 1) >= k:
                outputs.append(nums[d[0]])
                l += 1

            r += 1

        return outputs


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
