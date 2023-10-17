from typing import List


class Solution:
    def maxAreaBrute(self, height: List[int]) -> int:
        n = len(height)
        curr_max = 0
        for i in range(n):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                curr_max = max(area, curr_max)

        return curr_max

    # Key idea here is that we start with the widest tank. Clearly its a
    # good candidate due to it's width. Then we move the pointer at the
    # shorter wall since we are looking for the max area. If we move the
    # pointer at the longer wall, the height of the tank will remain the
    # same and width will decrease, hence the area will decrease.
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        curr_max = 0
        while l < r:
            if height[r] > height[l]:
                curr_max = max((r - l) * height[l], curr_max)
                l += 1
            else:
                curr_max = max((r - l) * height[r], curr_max)
                r -= 1
        return curr_max


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
